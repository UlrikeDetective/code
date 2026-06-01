const express = require('express');
const { Client } = require('pg');
const bodyParser = require('body-parser');
const path = require('path');
const session = require('express-session');

const app = express();
const port = process.env.PORT || 3005;

// DB Connection using environment variables or defaults
const db = new Client({
  host: process.env.POSTGRES_HOST || 'localhost',
  port: process.env.POSTGRES_PORT || 5432,
  user: process.env.POSTGRES_USER || 'postgres',
  password: process.env.POSTGRES_PASSWORD || '123456',
  database: 'books'
});

db.connect();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: true }));

// --- SESSION SETUP ---
app.use(session({
  secret: 'high-tide-books-secret',
  resave: false,
  saveUninitialized: true,
  cookie: { maxAge: 24 * 60 * 60 * 1000 } // 24 hours
}));

// --- GLOBAL MIDDLEWARE ---
// This makes currentCustomer available in all EJS templates and routes
app.use(async (req, res, next) => {
  res.locals.currentCustomer = null;
  res.locals.purchasedBookIds = [];
  res.locals.bookedEventIds = [];
  
  if (req.session.customerId) {
    try {
      const custRes = await db.query('SELECT * FROM customers WHERE id = $1', [req.session.customerId]);
      if (custRes.rows.length > 0) {
        res.locals.currentCustomer = custRes.rows[0];
        
        // Fetch IDs of books this customer has already bought
        const purchasedRes = await db.query(`
          SELECT DISTINCT book_id FROM order_items oi
          JOIN orders o ON oi.order_id = o.id
          WHERE o.customer_id = $1
        `, [req.session.customerId]);
        res.locals.purchasedBookIds = purchasedRes.rows.map(r => r.book_id);

        // Fetch IDs of events this customer has registered for
        const bookedRes = await db.query(
          'SELECT event_id FROM event_registrations WHERE customer_id = $1',
          [req.session.customerId]
        );
        res.locals.bookedEventIds = bookedRes.rows.map(r => r.event_id);
      }
    } catch (err) {
      console.error("Session Auth Error", err);
    }
  }
  next();
});

// --- ROUTES ---

// LOGIN: Handle persistent login via POST
app.post('/login', (req, res) => {
  const { customerId } = req.body;
  if (customerId) {
    req.session.customerId = customerId;
  }
  // Redirect back to wherever they were
  res.redirect(req.get('referer') || '/shop');
});

// LOGOUT: Clear session
app.post('/logout', (req, res) => {
  req.session.destroy();
  res.redirect('/shop');
});

// HOME - Entry Point
app.get('/', (req, res) => {
  res.render('index');
});

// BOOKSHOP - Books, Authors, Genres, Reviews
app.get('/shop', async (req, res) => {
  const search = req.query.search || '';
  try {
    let queryText = `
      SELECT b.id, b.title, a.first_name, a.last_name, g.name as genre, b.price, b.stock_quantity, b.hashtags
      FROM books b 
      JOIN authors a ON b.author_id = a.id 
      LEFT JOIN genres g ON b.genre_id = g.id
    `;
    let queryParams = [];

    if (search) {
      queryText += `
        WHERE b.title ILIKE $1 
        OR a.first_name ILIKE $1 
        OR a.last_name ILIKE $1 
        OR g.name ILIKE $1
        OR b.hashtags ILIKE $1
      `;
      queryParams.push(`%${search}%`);
    }

    const booksRes = await db.query(queryText, queryParams);
    const reviewsRes = await db.query(`
      SELECT r.rating, r.comment, b.title as book, c.first_name as customer
      FROM reviews r
      JOIN books b ON r.book_id = b.id
      JOIN customers c ON r.customer_id = c.id
      ORDER BY r.created_at DESC
    `);
    
    const allCustomersRes = await db.query('SELECT * FROM customers ORDER BY first_name');
    
    // --- RECOMMENDATIONS LOGIC ---
    let recommendations = [];
    if (req.session.customerId) {
      try {
        // 1. Hashtag Similarity: Find books with overlapping hashtags
        // We look for books that have at least one hashtag from the customer's bought books
        const hashtagRecs = await db.query(`
          WITH user_hashtags AS (
            SELECT DISTINCT unnest(string_to_array(replace(hashtags, '#', ''), ' ')) as tag
            FROM books b
            JOIN order_items oi ON b.id = oi.book_id
            JOIN orders o ON oi.order_id = o.id
            WHERE o.customer_id = $1 AND hashtags IS NOT NULL AND hashtags != ''
          )
          SELECT b.id, b.title, a.first_name, a.last_name, b.price, b.hashtags, 'Based on your interests' as reason
          FROM books b
          JOIN authors a ON b.author_id = a.id
          WHERE b.id NOT IN (
            SELECT book_id FROM order_items oi JOIN orders o ON oi.order_id = o.id WHERE o.customer_id = $1
          )
          AND b.stock_quantity > 0
          AND EXISTS (
            SELECT 1 FROM user_hashtags uh 
            WHERE b.hashtags ILIKE '%' || uh.tag || '%'
          )
          LIMIT 3
        `, [req.session.customerId]);

        // 2. Collaborative Filtering: "Customers who bought this also bought..."
        const collaborativeRecs = await db.query(`
          WITH similar_customers AS (
            SELECT DISTINCT o2.customer_id
            FROM orders o1
            JOIN order_items oi1 ON o1.id = oi1.order_id
            JOIN order_items oi2 ON oi1.book_id = oi2.book_id
            JOIN orders o2 ON oi2.order_id = o2.id
            WHERE o1.customer_id = $1 AND o2.customer_id != $1
          )
          SELECT b.id, b.title, a.first_name, a.last_name, b.price, b.hashtags, 'Others also liked' as reason
          FROM books b
          JOIN authors a ON b.author_id = a.id
          JOIN order_items oi ON b.id = oi.book_id
          JOIN orders o ON oi.order_id = o.id
          WHERE o.customer_id IN (SELECT customer_id FROM similar_customers)
          AND b.id NOT IN (
            SELECT book_id FROM order_items oi JOIN orders o ON oi.order_id = o.id WHERE o.customer_id = $1
          )
          AND b.stock_quantity > 0
          GROUP BY b.id, a.id
          ORDER BY COUNT(o.id) DESC
          LIMIT 3
        `, [req.session.customerId]);

        // Combine and de-duplicate recommendations
        const combined = [...hashtagRecs.rows, ...collaborativeRecs.rows];
        const seen = new Set();
        recommendations = combined.filter(b => {
          if (seen.has(b.id)) return false;
          seen.add(b.id);
          return true;
        });
      } catch (err) {
        console.error("Recommendation Error", err);
      }
    }

    res.render('shop', { 
      books: booksRes.rows, 
      reviews: reviewsRes.rows, 
      customers: allCustomersRes.rows,
      search: search,
      recommendations: recommendations
    });
  } catch (err) {
    console.error(err);
    res.send("DB Error");
  }
});

// CUSTOMER REVIEWS PAGE - See bought books and review them
app.get('/reviews', async (req, res) => {
  try {
    const allCustomersRes = await db.query('SELECT * FROM customers ORDER BY first_name');
    let boughtBooks = [];

    if (req.session.customerId) {
      // Fetch books this customer has actually bought AND their existing reviews
      const boughtRes = await db.query(`
        SELECT DISTINCT b.id, b.title, a.first_name, a.last_name,
               r.rating as existing_rating, r.comment as existing_comment
        FROM books b
        JOIN authors a ON b.author_id = a.id
        JOIN order_items oi ON b.id = oi.book_id
        JOIN orders o ON oi.order_id = o.id
        LEFT JOIN reviews r ON b.id = r.book_id AND r.customer_id = o.customer_id
        WHERE o.customer_id = $1
      `, [req.session.customerId]);
      boughtBooks = boughtRes.rows;
    }

    res.render('reviews', {
      customers: allCustomersRes.rows,
      boughtBooks: boughtBooks
    });
  } catch (err) {
    console.error(err);
    res.send("DB Error");
  }
});

// CUSTOMER: Register
app.post('/register', async (req, res) => {
  const { first_name, last_name, email } = req.body;
  try {
    const result = await db.query(
      'INSERT INTO customers (first_name, last_name, email) VALUES ($1, $2, $3) RETURNING id',
      [first_name, last_name, email]
    );
    req.session.customerId = result.rows[0].id;
    res.redirect('/shop');
  } catch (err) {
    console.error(err);
    res.send("Registration Error (Email might already exist)");
  }
});

// EVENTS - Events and Registrations
app.get('/events', async (req, res) => {
  try {
    // Fetch events with registration count, limited to top 100 upcoming
    const eventsRes = await db.query(`
      SELECT e.*, COUNT(er.customer_id) as reg_count
      FROM events e
      LEFT JOIN event_registrations er ON e.id = er.event_id
      WHERE e.event_date >= NOW()
      GROUP BY e.id
      ORDER BY e.event_date ASC
      LIMIT 100
    `);
    
    const regRes = await db.query(`
      SELECT e.name as event_name, c.first_name, c.last_name, er.registered_at
      FROM event_registrations er
      JOIN events e ON er.event_id = e.id
      JOIN customers c ON er.customer_id = c.id
      ORDER BY er.registered_at DESC
    `);

    const allCustomersRes = await db.query('SELECT * FROM customers ORDER BY first_name');
    
    res.render('events', { 
      events: eventsRes.rows, 
      registrations: regRes.rows,
      customers: allCustomersRes.rows
    });
  } catch (err) {
    console.error(err);
    res.send("DB Error");
  }
});

// BACKEND - Customers, Orders, Items, Authors, Genres
app.get('/admin', async (req, res) => {
  try {
    const customersRes = await db.query('SELECT * FROM customers');
    const ordersRes = await db.query(`
      SELECT o.id, c.first_name, c.last_name, o.order_date, o.total_amount 
      FROM orders o 
      JOIN customers c ON o.customer_id = c.id
      ORDER BY o.order_date DESC
      LIMIT 5
    `);
    const itemsRes = await db.query(`
      SELECT oi.order_id, b.title, oi.quantity, oi.unit_price 
      FROM order_items oi
      JOIN books b ON oi.book_id = b.id
      ORDER BY oi.id DESC
      LIMIT 5
    `);
    const authorsRes = await db.query('SELECT * FROM authors');
    const genresRes = await db.query('SELECT * FROM genres');
    const booksRes = await db.query('SELECT id, title, stock_quantity FROM books ORDER BY title');

    // --- DASHBOARD QUERIES ---
    
    // 1. Out of Stock
    const outOfStockRes = await db.query('SELECT title, stock_quantity FROM books WHERE stock_quantity = 0');

    // 2. Best Selling Books
    const bestSellersRes = await db.query(`
      SELECT b.title, SUM(oi.quantity) as total_sold
      FROM order_items oi
      JOIN books b ON oi.book_id = b.id
      GROUP BY b.id, b.title
      ORDER BY total_sold DESC
      LIMIT 5
    `);

    // 3. Best Selling Authors
    const topAuthorsRes = await db.query(`
      SELECT a.first_name, a.last_name, SUM(oi.quantity) as total_sold
      FROM order_items oi
      JOIN books b ON oi.book_id = b.id
      JOIN authors a ON b.author_id = a.id
      GROUP BY a.id, a.first_name, a.last_name
      ORDER BY total_sold DESC
      LIMIT 5
    `);

    // 4. Books that don't sell (Zero Sales)
    const zeroSalesRes = await db.query(`
      SELECT b.title FROM books b
      LEFT JOIN order_items oi ON b.id = oi.book_id
      GROUP BY b.id, b.title
      HAVING COUNT(oi.id) = 0
      LIMIT 10
    `);

    // 5. Top Customers (Highest Spenders)
    const topSpendersRes = await db.query(`
      SELECT c.first_name, c.last_name, SUM(o.total_amount) as total_spent
      FROM customers c
      JOIN orders o ON c.id = o.customer_id
      GROUP BY c.id
      ORDER BY total_spent DESC
      LIMIT 5
    `);

    // 6. Inactive Customers (No orders in last 3 months, or never)
    const inactiveCustomersRes = await db.query(`
      SELECT c.first_name, c.last_name, c.email, MAX(o.order_date) as last_order
      FROM customers c
      LEFT JOIN orders o ON c.id = o.customer_id
      GROUP BY c.id
      HAVING MAX(o.order_date) < NOW() - INTERVAL '3 months' OR MAX(o.order_date) IS NULL
      LIMIT 10
    `);

    // 7. Real Sales Data for Financials (Current Month)
    const currentMonthSalesRes = await db.query(`
      SELECT SUM(total_amount) as total FROM orders 
      WHERE order_date >= date_trunc('month', current_date)
    `);
    const currentMonthTicketsRes = await db.query(`
      SELECT COUNT(*) as count FROM event_registrations 
      WHERE registered_at >= date_trunc('month', current_date)
    `);

    res.render('admin', { 
      customers: customersRes.rows, 
      orders: ordersRes.rows, 
      items: itemsRes.rows,
      authors: authorsRes.rows,
      genres: genresRes.rows,
      books: booksRes.rows,
      stats: {
        outOfStock: outOfStockRes.rows,
        bestSellers: bestSellersRes.rows,
        topAuthors: topAuthorsRes.rows,
        zeroSales: zeroSalesRes.rows,
        topSpenders: topSpendersRes.rows,
        inactiveCustomers: inactiveCustomersRes.rows,
        currentMonthSales: currentMonthSalesRes.rows[0].total || 0,
        currentMonthTickets: currentMonthTicketsRes.rows[0].count || 0
      }
    });
  } catch (err) {
    console.error(err);
    res.send("DB Error");
  }
});

// FINANCIALS DASHBOARD - Business Plan & Real-time tracking
app.get('/admin/financials', async (req, res) => {
  try {
    // Current Month Totals
    const salesRes = await db.query(`
      SELECT COALESCE(SUM(total_amount), 0) as total FROM orders 
      WHERE order_date >= date_trunc('month', current_date)
    `);
    const ticketsRes = await db.query(`
      SELECT COUNT(*) as count FROM event_registrations 
      WHERE registered_at >= date_trunc('month', current_date)
    `);

    // Historical Performance (Last 6 Months)
    const historyRes = await db.query(`
      SELECT date_trunc('month', order_date) as month, SUM(total_amount) as total
      FROM orders
      WHERE order_date >= current_date - INTERVAL '6 months'
      GROUP BY month
      ORDER BY month DESC
    `);

    res.render('financials', {
      actualSales: parseFloat(salesRes.rows[0].total),
      actualTickets: parseInt(ticketsRes.rows[0].count),
      history: historyRes.rows.map(h => ({ ...h, total: parseFloat(h.total) })),
      // High Tide Plan Assumptions
      plan: {
        rent: 200,
        utilities: 75,
        helpers: 1800,
        ss_helpers: 576, // 32% of 1800
        autonomo: 310,
        misc: 50,
        book_margin_pct: 0.35,
        event_price: 15,
        event_margin: 13.64 // After 10% IVA
      }
    });
  } catch (err) {
    console.error(err);
    res.send("DB Error");
  }
});

// ADMIN: Restock Inventory
app.post('/admin/restock', async (req, res) => {
  const { book_id, additional_stock } = req.body;
  try {
    await db.query(
      'UPDATE books SET stock_quantity = stock_quantity + $1 WHERE id = $2',
      [additional_stock, book_id]
    );
    res.redirect('/admin');
  } catch (err) {
    console.error(err);
    res.send("Error updating stock");
  }
});

// --- POST ROUTES ---

// ADMIN: Add Book
app.post('/admin/add-book', async (req, res) => {
  const { title, author_first_name, author_last_name, genre_name, isbn, price, stock, pages, year, hashtags } = req.body;
  try {
    // 1. Get or Create Author
    let authorRes = await db.query(
      'SELECT id FROM authors WHERE first_name = $1 AND last_name = $2',
      [author_first_name, author_last_name]
    );
    let authorId;
    if (authorRes.rows.length > 0) {
      authorId = authorRes.rows[0].id;
    } else {
      const newAuthor = await db.query(
        'INSERT INTO authors (first_name, last_name) VALUES ($1, $2) RETURNING id',
        [author_first_name, author_last_name]
      );
      authorId = newAuthor.rows[0].id;
    }

    // 2. Get or Create Genre
    let genreRes = await db.query('SELECT id FROM genres WHERE name = $1', [genre_name]);
    let genreId;
    if (genreRes.rows.length > 0) {
      genreId = genreRes.rows[0].id;
    } else {
      const newGenre = await db.query(
        'INSERT INTO genres (name) VALUES ($1) RETURNING id',
        [genre_name]
      );
      genreId = newGenre.rows[0].id;
    }

    // 3. Insert Book
    await db.query(
      'INSERT INTO books (title, isbn, author_id, genre_id, price, stock_quantity, pages, released_year, hashtags) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)',
      [title, isbn, authorId, genreId, price, stock, pages, year, hashtags]
    );
    res.redirect('/admin');
  } catch (err) {
    console.error(err);
    res.send("Error adding book: " + err.message);
  }
});

// ADMIN: Add Event
app.post('/admin/add-event', async (req, res) => {
  const { name, date, location, description } = req.body;
  try {
    await db.query(
      'INSERT INTO events (name, event_date, location, description) VALUES ($1, $2, $3, $4)',
      [name, date, location, description]
    );
    res.redirect('/admin');
  } catch (err) {
    console.error(err);
    res.send("Error adding event");
  }
});

// CUSTOMER: Buy Book
app.post('/shop/buy', async (req, res) => {
  const { book_id, quantity } = req.body;
  const customer_id = req.session.customerId;
  
  if (!customer_id) return res.send("Please sign in first");
  
  try {
    // 1. Get book price
    const bookRes = await db.query('SELECT price FROM books WHERE id = $1', [book_id]);
    const price = bookRes.rows[0].price;
    const total = price * quantity;

    // 2. Create Order
    const orderRes = await db.query(
      'INSERT INTO orders (customer_id, total_amount) VALUES ($1, $2) RETURNING id',
      [customer_id, total]
    );
    const orderId = orderRes.rows[0].id;

    // 3. Create Order Item
    await db.query(
      'INSERT INTO order_items (order_id, book_id, quantity, unit_price) VALUES ($1, $2, $3, $4)',
      [orderId, book_id, quantity, price]
    );

    // 4. Update Stock
    await db.query('UPDATE books SET stock_quantity = stock_quantity - $1 WHERE id = $2', [quantity, book_id]);

    res.redirect('/shop');
  } catch (err) {
    console.error(err);
    res.send("Error processing purchase");
  }
});

// CUSTOMER: Write Review
app.post('/shop/review', async (req, res) => {
  const { book_id, rating, comment } = req.body;
  const customer_id = req.session.customerId;

  if (!customer_id) return res.send("Please sign in first");

  try {
    await db.query(
      'INSERT INTO reviews (book_id, customer_id, rating, comment) VALUES ($1, $2, $3, $4)',
      [book_id, customer_id, rating, comment]
    );
    res.redirect('/shop');
  } catch (err) {
    console.error(err);
    res.send("Error adding review (Maybe you already reviewed this book?)");
  }
});

// CUSTOMER: Register for Event
app.post('/events/register', async (req, res) => {
  const { event_id } = req.body;
  const customer_id = req.session.customerId;

  if (!customer_id) return res.send("Please sign in first");

  try {
    await db.query(
      'INSERT INTO event_registrations (event_id, customer_id) VALUES ($1, $2)',
      [event_id, customer_id]
    );
    res.redirect('/events');
  } catch (err) {
    console.error(err);
    res.send("Error registering for event");
  }
});

app.listen(port, () => {
  console.log(`[SYS] HackerBookshop listening at http://localhost:${port}`);
});

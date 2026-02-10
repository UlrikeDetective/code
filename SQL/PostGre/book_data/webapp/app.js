const express = require('express');
const { Client } = require('pg');
const bodyParser = require('body-parser');
const path = require('path');

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

// --- ROUTES ---

// HOME - Entry Point
app.get('/', (req, res) => {
  res.render('index');
});

// BOOKSHOP - Books, Authors, Genres, Reviews
app.get('/shop', async (req, res) => {
  const customerId = req.query.customerId;
  const search = req.query.search || '';
  try {
    let queryText = `
      SELECT b.id, b.title, a.first_name, a.last_name, g.name as genre, b.price, b.stock_quantity 
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
    
    let currentCustomer = null;
    if (customerId) {
      const custRes = await db.query('SELECT * FROM customers WHERE id = $1', [customerId]);
      currentCustomer = custRes.rows[0];
    }

    res.render('shop', { 
      books: booksRes.rows, 
      reviews: reviewsRes.rows, 
      customers: allCustomersRes.rows,
      currentCustomer: currentCustomer,
      search: search
    });
  } catch (err) {
    console.error(err);
    res.send("DB Error");
  }
});

// CUSTOMER REVIEWS PAGE - See bought books and review them
app.get('/reviews', async (req, res) => {
  const customerId = req.query.customerId;
  try {
    const allCustomersRes = await db.query('SELECT * FROM customers ORDER BY first_name');
    let currentCustomer = null;
    let boughtBooks = [];

    if (customerId) {
      const custRes = await db.query('SELECT * FROM customers WHERE id = $1', [customerId]);
      currentCustomer = custRes.rows[0];

      // Fetch books this customer has actually bought
      const boughtRes = await db.query(`
        SELECT DISTINCT b.id, b.title, a.first_name, a.last_name
        FROM books b
        JOIN authors a ON b.author_id = a.id
        JOIN order_items oi ON b.id = oi.book_id
        JOIN orders o ON oi.order_id = o.id
        WHERE o.customer_id = $1
      `, [customerId]);
      boughtBooks = boughtRes.rows;
    }

    res.render('reviews', {
      customers: allCustomersRes.rows,
      currentCustomer: currentCustomer,
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
    res.redirect(`/shop?customerId=${result.rows[0].id}`);
  } catch (err) {
    console.error(err);
    res.send("Registration Error (Email might already exist)");
  }
});

// EVENTS - Events and Registrations
app.get('/events', async (req, res) => {
  const customerId = req.query.customerId;
  try {
    // Only fetch events that haven't happened yet
    const eventsRes = await db.query('SELECT * FROM events WHERE event_date >= NOW() ORDER BY event_date ASC');
    const regRes = await db.query(`
      SELECT e.name as event_name, c.first_name, c.last_name, er.registered_at
      FROM event_registrations er
      JOIN events e ON er.event_id = e.id
      JOIN customers c ON er.customer_id = c.id
      ORDER BY er.registered_at DESC
    `);

    const allCustomersRes = await db.query('SELECT * FROM customers ORDER BY first_name');
    
    let currentCustomer = null;
    if (customerId) {
      const custRes = await db.query('SELECT * FROM customers WHERE id = $1', [customerId]);
      currentCustomer = custRes.rows[0];
    }

    res.render('events', { 
      events: eventsRes.rows, 
      registrations: regRes.rows,
      customers: allCustomersRes.rows,
      currentCustomer: currentCustomer
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
      SELECT o.id, c.email, o.order_date, o.total_amount 
      FROM orders o 
      JOIN customers c ON o.customer_id = c.id
    `);
    const itemsRes = await db.query(`
      SELECT oi.order_id, b.title, oi.quantity, oi.unit_price 
      FROM order_items oi
      JOIN books b ON oi.book_id = b.id
    `);
    const authorsRes = await db.query('SELECT * FROM authors');
    const genresRes = await db.query('SELECT * FROM genres');
    const booksRes = await db.query('SELECT id, title, stock_quantity FROM books ORDER BY title');
    
    res.render('admin', { 
      customers: customersRes.rows, 
      orders: ordersRes.rows, 
      items: itemsRes.rows,
      authors: authorsRes.rows,
      genres: genresRes.rows,
      books: booksRes.rows
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
  const { title, author_first_name, author_last_name, genre_name, price, stock, pages, year } = req.body;
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
      'INSERT INTO books (title, author_id, genre_id, price, stock_quantity, pages, released_year) VALUES ($1, $2, $3, $4, $5, $6, $7)',
      [title, authorId, genreId, price, stock, pages, year]
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
  const { book_id, customer_id, quantity } = req.body;
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
  const { book_id, customer_id, rating, comment } = req.body;
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
  const { event_id, customer_id } = req.body;
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

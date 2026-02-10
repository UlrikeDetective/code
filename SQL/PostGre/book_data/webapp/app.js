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
  try {
    const booksRes = await db.query(`
      SELECT b.id, b.title, a.first_name, a.last_name, g.name as genre, b.price, b.stock_quantity 
      FROM books b 
      JOIN authors a ON b.author_id = a.id 
      LEFT JOIN genres g ON b.genre_id = g.id
    `);
    const reviewsRes = await db.query(`
      SELECT r.rating, r.comment, b.title as book, c.first_name as customer
      FROM reviews r
      JOIN books b ON r.book_id = b.id
      JOIN customers c ON r.customer_id = c.id
    `);
    res.render('shop', { books: booksRes.rows, reviews: reviewsRes.rows });
  } catch (err) {
    console.error(err);
    res.send("DB Error: Check if 'books' database exists and tables are seeded.");
  }
});

// EVENTS - Events and Registrations
app.get('/events', async (req, res) => {
  try {
    const eventsRes = await db.query('SELECT * FROM events');
    const regRes = await db.query(`
      SELECT e.name as event_name, c.first_name, c.last_name, er.registered_at
      FROM event_registrations er
      JOIN events e ON er.event_id = e.id
      JOIN customers c ON er.customer_id = c.id
    `);
    res.render('events', { events: eventsRes.rows, registrations: regRes.rows });
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
    
    res.render('admin', { 
      customers: customersRes.rows, 
      orders: ordersRes.rows, 
      items: itemsRes.rows,
      authors: authorsRes.rows,
      genres: genresRes.rows
    });
  } catch (err) {
    console.error(err);
    res.send("DB Error");
  }
});

// --- POST ROUTES ---

// ADMIN: Add Book
app.post('/admin/add-book', async (req, res) => {
  const { title, author_id, genre_id, price, stock, pages, year } = req.body;
  try {
    await db.query(
      'INSERT INTO books (title, author_id, genre_id, price, stock_quantity, pages, released_year) VALUES ($1, $2, $3, $4, $5, $6, $7)',
      [title, author_id, genre_id, price, stock, pages, year]
    );
    res.redirect('/admin');
  } catch (err) {
    console.error(err);
    res.send("Error adding book");
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

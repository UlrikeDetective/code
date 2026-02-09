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
      SELECT b.title, a.first_name, a.last_name, g.name as genre, b.price, b.stock_quantity 
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

// BACKEND - Customers, Orders, Items
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
    res.render('admin', { customers: customersRes.rows, orders: ordersRes.rows, items: itemsRes.rows });
  } catch (err) {
    console.error(err);
    res.send("DB Error");
  }
});

app.listen(port, () => {
  console.log(`[SYS] HackerBookshop listening at http://localhost:${port}`);
});

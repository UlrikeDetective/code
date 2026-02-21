select * from authors;
select * from books order by id desc;
select * from genres;
select * from events;
select * from event_registrations;
select * from customers order by id desc;
select * from order_items order by id desc;
select * from orders order by id desc;
select * from reviews;


SELECT * FROM authors WHERE first_name = 'Toby';
Select * From books where author_id = 12;

-- BOOKSHOP BUSINESS OVERVIEW --
-- Current System Date for context: 2026-02-21

-- 1. CUSTOMER METRICS
-- Total number of customers
SELECT COUNT(*) AS total_customers 
FROM customers;

-- New customers joined in the last month (since 2026-01-21)
SELECT COUNT(*) AS new_customers_last_month 
FROM customers 
WHERE joined_date >= '2026-02-21'::timestamp - INTERVAL '1 month';


-- 2. SALES PERFORMANCE
-- Total books sold per title (Top 15)
-- This tracks actual volume of sales from the order_items table
SELECT b.title, SUM(oi.quantity) AS total_units_sold
FROM order_items oi
JOIN books b ON oi.book_id = b.id
GROUP BY b.id, b.title
ORDER BY total_units_sold DESC
LIMIT 15;

-- Best-selling Authors by quantity sold
SELECT a.first_name, a.last_name, SUM(oi.quantity) AS units_sold
FROM order_items oi
JOIN books b ON oi.book_id = b.id
JOIN authors a ON b.author_id = a.id
GROUP BY a.id, a.first_name, a.last_name
ORDER BY units_sold DESC
LIMIT 10;

-- Revenue by Genre
-- Shows which categories are the most profitable
SELECT g.name AS genre, SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM order_items oi
JOIN books b ON oi.book_id = b.id
JOIN genres g ON b.genre_id = g.id
GROUP BY g.id, g.name
ORDER BY total_revenue DESC;


-- 3. INVENTORY & STOCK MANAGEMENT
-- Current stock levels (Lowest stock first, highlighting items needing reorder)
SELECT title, stock_quantity, price
FROM books
ORDER BY stock_quantity ASC
LIMIT 20;

-- Books currently Out of Stock
SELECT title, isbn, released_year
FROM books
WHERE stock_quantity = 0;


-- 4. SOCIAL ENGAGEMENT (REVIEWS)
-- Highest rated books (with at least 2 reviews)
SELECT b.title, ROUND(AVG(r.rating), 2) AS avg_rating, COUNT(r.id) AS review_count
FROM reviews r
JOIN books b ON r.book_id = b.id
GROUP BY b.id, b.title
HAVING COUNT(r.id) >= 2
ORDER BY avg_rating DESC, review_count DESC;


-- 5. EVENT PERFORMANCE
-- Registrations per event (Upcoming and Past)
SELECT e.name AS event_name, e.event_date, COUNT(er.customer_id) AS total_registrations
FROM events e
LEFT JOIN event_registrations er ON e.id = er.event_id
GROUP BY e.id, e.name, e.event_date
ORDER BY e.event_date ASC;

-- Most popular event locations
SELECT location, COUNT(*) AS event_count
FROM events
GROUP BY location;


-- 6. FINANCIAL OVERVIEW
-- Total Revenue to date
SELECT SUM(total_amount) AS total_lifetime_revenue 
FROM orders;

-- Top 5 spending customers (Customer Lifetime Value)
SELECT c.first_name, c.last_name, c.email, SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.first_name, c.last_name, c.email
ORDER BY total_spent DESC
LIMIT 5;

-- Average Order Value
SELECT ROUND(AVG(total_amount), 2) AS average_order_value 
FROM orders;


INSERT INTO books (title, author_id, genre_id, released_year, price, stock_quantity, pages) VALUES
('Paradise Crime Thrillers - Vol 02 - Wired rogue', 12, 7, 2016, 9.99, 10, 297),
('Paradise Crime Thrillers - Vol 03 - Wired hard', 12, 7, 2017, 9.99, 10, 281),
('Paradise Crime Thrillers - Vol 04 - Wired dark', 12, 7, 2017, 9.99, 10, 279),
('Paradise Crime Thrillers - Vol 05 - Wired dawn', 12, 7, 2018, 9.99, 10, 299),
('Paradise Crime Thrillers - Vol 06 - Wired justice', 12, 7, 2018, 9.99, 10, 301),
('Paradise Crime Thrillers - Vol 07 - Wired secret', 12, 7, 2018, 9.99, 10, 283),
('Paradise Crime Thrillers - Vol 08 - Wired fear', 12, 7, 2019, 9.99, 10, 286),
('Paradise Crime Thrillers - Vol 10 - Wired courage', 12, 7, 2019, 9.99, 10, 298),
('Paradise Crime Thrillers - Vol 11 - Wired truth', 12, 7, 2020, 9.99, 10, 269),
('Paradise Crime Thrillers - Vol 12 - Wired ghost', 12, 7, 2020, 9.99, 10, 293),
('Paradise Crime Thrillers - Vol 13 - Wired strong', 12, 7, 2020, 9.99, 10, 295),
('Paradise Crime Thrillers - Vol 14 - Wired revenge', 12, 7, 2021, 9.99, 10, 284),
('Paradise Crime Thrillers - Vol 15 - Wired target', 12, 7, 2022, 9.99, 10, 293);
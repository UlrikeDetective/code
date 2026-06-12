-- ==========================================================
-- BOOKSHOP BUSINESS OVERVIEW REPORT
-- ==========================================================
-- Current System Date: 2026-02-21

-- 1. QUICK SYSTEM CHECKS (Basic Table Dumps)
-- ==========================================================
-- These help verify data integrity at a glance
SELECT * FROM authors order by id;
SELECT * FROM books ORDER BY id desc;
SELECT * FROM customers ORDER BY id DESC;
SELECT * FROM orders ORDER BY id DESC;
Select * from order_items order by id desc;
Select * from genres order by id;
select * from events order by event_date;
select * from event_registrations order by registered_at desc;
select * from reviews order by id desc;

select * from authors where last_name = 'Kerouac';
select * from books where author_id = 96;
SELECT * FROM customers where last_name = 'Müller';
select * from events where event_date >= current_date order by event_date;

-- 2. CUSTOMER METRICS
-- ==========================================================
-- Total number of customers
SELECT COUNT(*) AS total_customers 
FROM customers;

-- New customers joined in the last month
SELECT COUNT(*) AS new_customers_last_month 
FROM customers 
WHERE joined_date >= CURRENT_DATE - INTERVAL '1 month';

-- New customers joined in the last ... for dashboard
SELECT 
    COUNT(*) FILTER (WHERE joined_date >= NOW() - INTERVAL '1 day') AS last_24h,
    COUNT(*) FILTER (WHERE joined_date >= CURRENT_DATE - INTERVAL '7 days') AS last_week,
    COUNT(*) FILTER (WHERE joined_date >= CURRENT_DATE - INTERVAL '1 month') AS last_month,
    COUNT(*) FILTER (WHERE joined_date >= CURRENT_DATE - INTERVAL '3 months') AS last_quarter,
    COUNT(*) FILTER (WHERE joined_date >= CURRENT_DATE - INTERVAL '1 year') AS last_year
FROM customers;


-- 3. SALES PERFORMANCE
-- ==========================================================
-- Top 15 Best Selling Books (by Volume)
SELECT b.title, SUM(oi.quantity) AS total_units_sold
FROM order_items oi
JOIN books b ON oi.book_id = b.id
GROUP BY b.id, b.title
ORDER BY total_units_sold DESC
LIMIT 15;

-- Books with ZERO Sales (Using LEFT JOIN to find unsold inventory)
SELECT b.title, COALESCE(SUM(oi.quantity), 0) AS total_units_sold
FROM books b
LEFT JOIN order_items oi ON b.id = oi.book_id
GROUP BY b.id, b.title
HAVING COALESCE(SUM(oi.quantity), 0) = 0
ORDER BY b.title ASC
LIMIT 250;

-- Best-selling Authors by quantity sold
SELECT a.first_name, a.last_name, SUM(oi.quantity) AS units_sold
FROM order_items oi
JOIN books b ON oi.book_id = b.id
JOIN authors a ON b.author_id = a.id
GROUP BY a.id, a.first_name, a.last_name
ORDER BY units_sold DESC
LIMIT 25;

-- Revenue by Genre
SELECT g.name AS genre, SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM order_items oi
JOIN books b ON oi.book_id = b.id
JOIN genres g ON b.genre_id = g.id
GROUP BY g.id, g.name
ORDER BY total_revenue DESC;

-- Change prices on books
SELECT * FROM authors where last_name = 'Pullman';
SELECT * FROM books where author_id = 105;


-- 4. INVENTORY & STOCK MANAGEMENT
-- ==========================================================
-- Critical Stock Levels (Lowest stock first)
SELECT title, stock_quantity, price
FROM books
ORDER BY stock_quantity ASC
LIMIT 20;

-- Current Out of Stock List
SELECT title, isbn, released_year
FROM books
WHERE stock_quantity = 0;

SELECT * FROM books ORDER BY price;

-- 5. SOCIAL & EVENT ENGAGEMENT
-- ==========================================================
-- Highest Rated Books (with at least 2 reviews)
SELECT b.title, ROUND(AVG(r.rating), 2) AS avg_rating, COUNT(r.id) AS review_count
FROM reviews r
JOIN books b ON r.book_id = b.id
GROUP BY b.id, b.title
HAVING COUNT(r.id) >= 2
ORDER BY avg_rating DESC, review_count DESC;

-- Registrations per event
SELECT e.name AS event_name, e.event_date, COUNT(er.customer_id) AS total_registrations
FROM events e
LEFT JOIN event_registrations er ON e.id = er.event_id
GROUP BY e.id, e.name, e.event_date
-- ORDER BY e.event_date ASC;
Order by t


-- 6. FINANCIAL OVERVIEW
-- ==========================================================
-- Total Revenue to date
SELECT SUM(total_amount) AS total_lifetime_revenue 
FROM orders;

SELECT 
    SUM(total_amount) FILTER (WHERE order_date >= NOW() - INTERVAL '1 day') AS rev_last_24h,
    SUM(total_amount) FILTER (WHERE order_date >= CURRENT_DATE - INTERVAL '7 days') AS rev_last_week,
    SUM(total_amount) FILTER (WHERE order_date >= CURRENT_DATE - INTERVAL '1 month') AS rev_last_month,
    SUM(total_amount) FILTER (WHERE order_date >= CURRENT_DATE - INTERVAL '3 months') AS rev_last_quarter,
    SUM(total_amount) FILTER (WHERE order_date >= CURRENT_DATE - INTERVAL '1 year') AS rev_last_year
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


 --  Customers who bought books by Philip Pullman:
SELECT DISTINCT c.first_name, c.last_name, c.email
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN books b ON oi.book_id = b.id
JOIN authors a ON b.author_id = a.id
WHERE a.first_name = 'Toby' AND a.last_name = 'Neal';

 -- Customers who bought 'Hula':

SELECT DISTINCT c.first_name, c.last_name, c.email
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN books b ON oi.book_id = b.id
WHERE b.title = 'Normal People';

 -- Customers who bought books with hashtag 'tech':

SELECT DISTINCT c.first_name, c.last_name, c.email, b.title
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN books b ON oi.book_id = b.id
WHERE b.hashtags LIKE '%#singapore%';

SELECT * FROM books where title = 'Barbarian - Days A Surfing Life';

SELECT DISTINCT c.first_name, c.last_name, c.email
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN books b ON oi.book_id = b.id
JOIN authors a ON b.author_id = a.id
-- WHERE b.title = ''Aloha Kitchen: Recipes from Hawai'i'';
Where b.author_id = 198;

SELECT * FROM authors where last_name = 'Kysar';

-- Amount Paid per Customer
-- This query groups the results by customer and sums their total spend on 'Palo Alto', in case a customer bought it across multiple orders.
SELECT
c.first_name,
c.last_name,
c.email,
SUM(oi.quantity * oi.unit_price) AS total_paid
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN books b ON oi.book_id = b.id
WHERE b.title = 'Palo Alto'
GROUP BY c.id, c.first_name, c.last_name, c.email;

-- Total Money Made from the Book
-- This query calculates the total revenue generated specifically from 'Palo Alto' across the entire shop.

SELECT
b.title,
SUM(oi.quantity * oi.unit_price) AS total_revenue,
SUM(oi.quantity) AS total_units_sold
FROM books b
JOIN order_items oi ON b.id = oi.book_id
WHERE b.title = 'Palo Alto'
GROUP BY b.id, b.title;

-- which persons bought a book but haven't registered to the book event.
SELECT DISTINCT c.first_name, c.last_name, c.email
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN books b ON oi.book_id = b.id
WHERE b.title = 'Normal People'
  -- Filter out customers who ARE registered for event 12
  AND NOT EXISTS (
      SELECT 1 
      FROM event_registrations er 
      WHERE er.customer_id = c.id 
        AND er.event_id = 12
  );

  select * from events order by event_date;

  SELECT DISTINCT c.first_name, c.last_name, c.email
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN books b ON oi.book_id = b.id
WHERE b.title = 'Steve Jobs in Exile: The Untold Story of NeXT and the Remaking of an American Visionary'
  -- Filter out customers who ARE registered for event 12
  AND NOT EXISTS (
      SELECT 1 
      FROM event_registrations er 
      WHERE er.customer_id = c.id 
        AND er.event_id = 76
  );

    SELECT DISTINCT c.first_name, c.last_name, c.email
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN books b ON oi.book_id = b.id
WHERE b.hashtags LIKE '%#romance%'
  AND NOT EXISTS (
      SELECT 1 
      FROM event_registrations er 
      WHERE er.customer_id = c.id 
        AND er.event_id = 13
  );

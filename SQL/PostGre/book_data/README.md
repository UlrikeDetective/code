# High Tide Books - SQL Learning Project

A comprehensive practice environment for mastering PostgreSQL, relational database design, and web integration. This project simulates a modern, high-volume bookshop, featuring session-based authentication, a Business Intelligence dashboard, and a recommendation engine.

## 📚 Project Overview

This project is divided into two main parts:
1.  **SQL Core**: Normalized schema design, data seeding, and business reporting scripts.
2.  **Web Application**: A Node.js/Express interface featuring persistent login sessions, real-time management dashboards, and predictive recommendations.

## 🚀 Getting Started

### 1. Database Setup
Ensure you have **PostgreSQL** installed and running.

1.  Create a database named `books`:
    ```sql
    CREATE DATABASE books;
    ```
2.  Initialize the schema:
    - `psql -d books -f sql/book_tables_improved.sql`
3.  Seed the data:
    - `psql -d books -f sql/book_data_improved.sql`

### 2. Web Application Setup
1.  Navigate to the webapp directory:
    ```bash
    cd webapp
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Start the server:
    ```bash
    node app.js
    ```
4.  Open your browser at `http://localhost:3005`.

## 📂 Directory Structure

- `sql/`: PostgreSQL scripts.
  - `book_tables_improved.sql`: The final normalized schema.
  - `overview.sql`: Collection of BI queries for system reporting.
- `webapp/`: Node.js/Express application.
  - `views/`: Session-aware EJS templates.
  - `public/`: Modern Stockholm-inspired CSS.

## 🛠 Features
- **Persistent Sessions**: Sign in once and stay logged in across all store pages.
- **Searchable Autocomplete**: Fast customer and book selection in forms using searchable `<datalist>` inputs.
- **Recommendation Engine**: Personalized book suggestions based on hashtag similarity and collaborative filtering.
- **BI Dashboard**: Real-time admin reporting on best sellers, out-of-stock items, and VIP customers.
- **Financial Dashboard**: Real-time P&L tracking and break-even analysis against a fixed cost structure.
- **Inventory Visuals**: Public shop filters out zero-stock items; "OWNED" markers for purchased books.
- **Verified Reviews**: Reading journal that tracks purchase history and prevents duplicate reviews.
- **Event Tracking**: Real-time booking status identifying if a customer has already reserved a spot.
- **Search System**: Case-insensitive partial matching for books, authors, genres, and hashtags.

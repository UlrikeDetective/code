# Stockholm Bookshop - SQL Learning Project

A comprehensive practice environment for mastering PostgreSQL, relational database design, and web integration. This project simulates a modern bookshop in Stockholm, featuring session-based authentication and a Business Intelligence dashboard.

## 📚 Project Overview

This project is divided into two main parts:
1.  **SQL Core**: Normalized schema design, data seeding, and business reporting scripts.
2.  **Web Application**: A Node.js/Express interface featuring persistent login sessions and real-time management dashboards.

## 🚀 Getting Started

### 1. Database Setup
Ensure you have **PostgreSQL** installed and running.

1.  Create a database named `books`:
    ```sql
    CREATE DATABASE books;
    ```
2.  Initialize the schema:
    - Advanced version: `psql -d books -f sql/book_tables_improved.sql`
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
- **BI Dashboard**: Real-time admin reporting on best sellers, out-of-stock items, and VIP customers.
- **Inventory Visuals**: Catalog markers for "OWNED" books and low-stock alerts.
- **Verified Reviews**: Reading journal that tracks purchase history and prevents duplicate reviews.
- **Event Tracking**: Real-time registration counters for community events.
- **Search System**: Case-insensitive partial matching for books, authors, and genres.

# Stockholm Bookshop - SQL Learning Project

A comprehensive practice environment for mastering PostgreSQL, relational database design, and web integration. This project simulates a fictional bookshop in Stockholm, evolving from a single-table setup to a fully normalized relational schema.

## 📚 Project Overview

This project is divided into two main parts:
1.  **SQL Core**: A collection of scripts for schema design, data seeding, and analytical queries.
2.  **Web Application**: A modern, minimalist Node.js/Express interface for interacting with the database.

## 🚀 Getting Started

### 1. Database Setup
Ensure you have **PostgreSQL** installed and running.

1.  Create a database named `books`:
    ```sql
    CREATE DATABASE books;
    ```
2.  Initialize the schema:
    - For the basic version: `psql -d books -f sql/book_tables.sql`
    - For the advanced version: `psql -d books -f sql/book_tables_improved.sql`
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
3.  Configure environment variables (optional, defaults are used in `app.js`):
    - `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_USER`, `POSTGRES_PASSWORD`
4.  Start the server:
    ```bash
    node app.js
    ```
5.  Open your browser at `http://localhost:3005`.

## 📂 Directory Structure

- `sql/`: Contains all PostgreSQL scripts.
  - `book_tables_improved.sql`: The final normalized schema.
  - `book_data_improved.sql`: Comprehensive seed data.
  - `book_data_queries.sql`: Practice queries for analysis.
- `webapp/`: Node.js/Express application.
  - `views/`: EJS templates (Shop, Reviews, Events, Admin).
  - `public/`: Modern Stockholm-inspired CSS and assets.

## 🛠 Features
- **Modern UI**: Clean, Stockholm-inspired design with a focus on whitespace and typography.
- **Dynamic Catalog**: Browse, search, and filter books by title, author, or genre.
- **Order Management**: Real-time stock updates and order tracking.
- **Customer Journal**: Purchase-verified book reviews.
- **Event Scheduling**: Management for community store events.
- **Admin Dashboard**: Catalog management, restocking, and sales monitoring.

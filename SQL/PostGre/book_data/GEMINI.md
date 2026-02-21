# Stockholm Bookshop - SQL & Web Project Context

This project is a comprehensive learning environment focused on mastering PostgreSQL, relational database design (3NF), and web integration using Node.js and Express. It simulates a fictional bookshop in Stockholm, evolving from flat data structures to a fully normalized relational schema.

## 🚀 Project Overview

- **Purpose**: Educational project for database normalization, advanced SQL queries, and CRUD web development.
- **Main Technologies**:
  - **Database**: PostgreSQL
  - **Backend**: Node.js, Express, `pg` (node-postgres)
  - **Frontend**: EJS (Embedded JavaScript), Vanilla CSS (Stockholm Minimalist design)
- **Architecture**: A classic 3nd Normal Form (3NF) schema with a Node.js middleware layer handling business logic such as inventory management and transaction-verified reviews.

## 🏗 Database Schema (books)

The database `books` consists of the following normalized tables:
- `authors`: Writer biographies and names.
- `genres`: Book categories.
- `books`: Central hub linking authors and genres, including stock and pricing.
- `customers`: User identity management.
- `orders` & `order_items`: Transactional history.
- `reviews`: Customer feedback (unique per book/customer).
- `events` & `event_registrations`: Community engagement tracking.

## 🛠 Building and Running

### Database Setup
1.  **Create Database**: `CREATE DATABASE books;`
2.  **Initialize Schema**: `psql -d books -f sql/book_tables_improved.sql`
3.  **Seed Data**: `psql -d books -f sql/book_data_improved.sql`

### Web Application
1.  **Navigate**: `cd webapp`
2.  **Install**: `npm install`
3.  **Start**: `node app.js` (Defaults to port `3005`)
4.  **Environment Variables**:
    - `POSTGRES_HOST` (default: `localhost`)
    - `POSTGRES_PORT` (default: `5432`)
    - `POSTGRES_USER` (default: `postgres`)
    - `POSTGRES_PASSWORD` (default: `123456`)

## 📏 Development Conventions

### SQL Standards
- **Normalization**: Always aim for 3NF to avoid data redundancy.
- **Search**: Use `ILIKE` for case-insensitive partial matching in the web search filter.
- **Integrity**: Use `CHECK` constraints for prices and stock quantities (must be non-negative).
- **Constraints**: Enforce business rules at the database level where possible (e.g., `UNIQUE(book_id, customer_id)` in reviews).

### Web & API Logic
- **Business Logic**: Inventory updates (stock decrements) and order creation are handled sequentially in the `/shop/buy` route.
- **Verified Reviews**: Logic in `/reviews` ensures customers can only review books they have actually purchased.
- **View Engine**: EJS templates are used for server-side rendering, located in `webapp/views/`.

### Design System (Stockholm Minimalist)
- **Primary Color**: `#4A90E2` (Sky Blue)
- **Background**: `#F8F8F8`
- **Typography**: Clean, monospace font for a "modern technical" aesthetic.
- **Focus**: High whitespace and clear typography.

## 📂 Key Files
- `sql/book_tables_improved.sql`: The primary schema definition.
- `sql/book_data_improved.sql`: Comprehensive seed data for testing.
- `webapp/app.js`: Main Express application and database route handlers.
- `PROJECT.md`: Detailed architectural decisions and learning milestones.

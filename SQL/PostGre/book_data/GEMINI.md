# High Tide Books - SQL & Web Project Context

This project is a comprehensive learning environment focused on mastering PostgreSQL, relational database design (3NF), and web integration using Node.js and Express. It simulates a modern, high-volume bookshop, evolving from flat data structures to a fully normalized relational schema.

## 🚀 Project Overview

- **Purpose**: Educational project for database normalization, advanced SQL queries, recommendation engines, and CRUD web development.
- **Main Technologies**:
  - **Database**: PostgreSQL
  - **Backend**: Node.js, Express, `express-session`, `pg` (node-postgres)
  - **Frontend**: EJS (Embedded JavaScript), Vanilla CSS (Stockholm Minimalist design)
- **Architecture**: A 3rd Normal Form (3NF) schema with a Node.js middleware layer handling business logic, session-based authentication, and business intelligence reporting.

## 🏗 Database Schema (books)

The database `books` consists of the following normalized tables:
- `authors`: Writer biographies and names.
- `genres`: Book categories.
- `books`: Central hub linking authors and genres, including stock, pricing, and hashtags.
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
2.  **Install**: `npm install` (Requires `express-session`)
3.  **Start**: `node app.js` (Defaults to port `3005`)
4.  **Environment Variables**:
    - `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_USER`, `POSTGRES_PASSWORD`

## 📏 Development Conventions

### Authentication & Sessions
- **Persistent State**: Uses `express-session` to keep customers logged in across pages.
- **Middleware**: Global middleware in `app.js` fetches `currentCustomer`, `purchasedBookIds`, and `bookedEventIds` for every request.
- **Auth Flow**: Users sign in via POST to `/login` (using a searchable autocomplete field) and sign out via `/logout`.

### SQL & Business Intelligence
- **Normalization**: Always maintain 3NF integrity.
- **BI Dashboard**: The Admin page tracks out-of-stock items, best-sellers, VIP customers, and churn risk.
- **Financial Dashboard**: Tracks real-time P&L against a fixed cost structure (Rent, Staff, Social Security, etc.) and break-even analysis.
- **Recommendations**: Implements hashtag-based similarity and collaborative filtering ("Others also liked") to suggest new books to customers.

### UI & UX Logic
- **Searchable Selection**: Uses `<datalist>` for fast customer and book selection in forms.
- **Inventory Filtering**: The public shop view automatically hides out-of-stock items.
- **Event Status**: Real-time feedback showing "BOOKED" status for events already reserved by the customer.
- **Feedback**: Books are marked as "OWNED" in the shop if purchased; reviews are verified to prevent duplicates.

## 📂 Key Files
- `sql/book_tables_improved.sql`: The primary schema definition.
- `sql/overview.sql`: Business report query collection.
- `webapp/app.js`: Main logic, session management, recommendation engine, and BI queries.
- `webapp/views/financials.ejs`: Financial dashboard view with cost structure analysis.
- `PROJECT.md`: Architectural decisions and milestones.

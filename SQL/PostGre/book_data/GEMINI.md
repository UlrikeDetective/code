# Stockholm Bookshop - SQL & Web Project Context

This project is a comprehensive learning environment focused on mastering PostgreSQL, relational database design (3NF), and web integration using Node.js and Express. It simulates a fictional bookshop in Stockholm, evolving from flat data structures to a fully normalized relational schema.

## 🚀 Project Overview

- **Purpose**: Educational project for database normalization, advanced SQL queries, and CRUD web development.
- **Main Technologies**:
  - **Database**: PostgreSQL
  - **Backend**: Node.js, Express, `express-session`, `pg` (node-postgres)
  - **Frontend**: EJS (Embedded JavaScript), Vanilla CSS (Stockholm Minimalist design)
- **Architecture**: A 3rd Normal Form (3NF) schema with a Node.js middleware layer handling business logic, session-based authentication, and business intelligence reporting.

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
2.  **Install**: `npm install` (Requires `express-session`)
3.  **Start**: `node app.js` (Defaults to port `3005`)
4.  **Environment Variables**:
    - `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_USER`, `POSTGRES_PASSWORD`

## 📏 Development Conventions

### Authentication & Sessions
- **Persistent State**: Uses `express-session` to keep customers logged in across pages.
- **Middleware**: Global middleware in `app.js` fetches `currentCustomer` and `purchasedBookIds` for every request.
- **Auth Flow**: Users sign in via POST to `/login` and sign out via `/logout`.

### SQL & Business Intelligence
- **Normalization**: Always maintain 3NF integrity.
- **BI Dashboard**: The Admin page uses complex aggregations to track:
    - Out of stock items.
    - Best-selling books and authors by volume.
    - Non-performing inventory (zero sales).
    - VIP customers (highest spenders).
    - Inactive customers (churn risk).
- **Integrity**: Enforce non-negative stock and unique reviews at the DB level.

### UI & UX Logic
- **Feedback**: Books are marked as "OWNED" in the shop if purchased.
- **Verification**: Reviews are verified; existing reviews are displayed instead of the "Write Review" button.
- **Dashboards**: Real-time registration counts on the Events page.
- **Streamlined Admin**: Focused on BI and recent transactions (limited to latest 5 entries).

## 📂 Key Files
- `sql/book_tables_improved.sql`: The primary schema definition.
- `sql/overview.sql`: Business report query collection.
- `webapp/app.js`: Main logic, session management, and BI queries.
- `PROJECT.md`: Architectural decisions and milestones.

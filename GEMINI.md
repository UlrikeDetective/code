# SQL Code Repository - GEMINI Context

This repository is a comprehensive collection of SQL learning resources, practice scripts, and web application prototypes covering MySQL, PostgreSQL, and Google BigQuery. It also includes several Node.js applications that demonstrate how to integrate these databases into web environments.

## Project Structure

### Databases & SQL
- **MySQL**: Located in `SQL/MySQL/` and `SQL/node-and-mysql/`. Includes world data, user schemas, and practice scripts.
- **PostgreSQL**: Located in `SQL/PostGre/`. Includes complex projects like `instagram_clone`, `music-app`, and various travel trackers.
- **BigQuery**: Located in `SQL/BigQuery/`. Focuses on e-commerce datasets (`thelook_ecommerce`).

### Web Applications (Node.js)
The project contains several prototypes built with Express and EJS:
- **Travel Tracker**:
  - PostgreSQL version: `SQL/PostGre/8.5 Family Travel Tracker/`
  - MySQL version: `SQL/MySQL/visited_countries/`
- **Join Us**: `SQL/node-and-mysql/JoinUs/` - A lead generation landing page prototype.
- **Music App**: `SQL/PostGre/music-app/` - A simple music collection manager.
- **Instagram Clone**: `SQL/PostGre/instagram_clone/` - Database schema and queries for a social media clone.

## Key Technologies
- **Backend**: Node.js, Express
- **Frontend**: EJS (Embedded JavaScript), CSS
- **Databases**: MySQL (`mysql`, `mysql2`), PostgreSQL (`pg`), BigQuery
- **Data Generation**: Faker (used for seeding databases)

## Development Conventions
- **Database Connections**: Many projects use hardcoded connection strings for local development (typically `localhost`, `postgres`/`root` users). **Note**: Transitioning to environment variables is a suggested improvement.
- **SQL Styling**: SQL scripts generally follow standard uppercase keyword conventions.
- **Project Type**: Hybrid (Data-focused with Web Prototypes).

## Building and Running

### Node.js Applications
To run any of the web applications, navigate to its directory and use:
```bash
npm install
node <main_file>.js  # Often index.js or app.js
```
*Check the specific `package.json` in each subdirectory for the entry point.*

### SQL Scripts
SQL scripts can be executed using their respective CLI tools or GUI managers (like pgAdmin, MySQL Workbench, or BigQuery Console).
- MySQL: `mysql -u <user> -p <database> < script.sql`
- PostgreSQL: `psql -U <user> -d <database> -f script.sql`

## TODOs & Future Exploration
- [ ] Transition hardcoded credentials to `.env` files.
- [ ] Connect the `coffee_shop.py` (Python) logic to a MySQL database.
- [ ] Explore BigQuery to MySQL data migration.
- [ ] Debug existing Node.js app connection issues.

## Important Files
- `SQL/PostGre/instagram_clone/schema.sql`: Comprehensive social media database schema.
- `SQL/BigQuery/thelook_ecommerce/Thelook_others/schemas.txt`: Metadata for BigQuery e-commerce practice.
- `todos.txt`: Personal learning roadmap.

# Project Specification: Database Learning Journey

This document outlines the architectural decisions and learning milestones achieved during the development of the Stockholm Bookshop project.

## 🎯 Learning Objectives

- **Relational Design**: Transitioning from "flat" data (CSV-style) to a normalized schema (3NF).
- **Advanced SQL**: Practicing Joins (INNER, LEFT), Aggregations (COUNT, SUM, AVG), and complex filtering (ILIKE, CASE).
- **CRUD Operations**: Implementing Create, Read, Update, and Delete logic via a web interface.
- **Transaction Logic**: Handling inventory management where a "Buy" action impacts multiple tables (`orders`, `order_items`, `books`).

## 🏗 Database Architecture

The project uses a normalized schema to ensure data integrity:

- **authors**: Stores writer biographies and names.
- **genres**: Categorizes books.
- **books**: The central hub, linking authors and genres.
- **customers**: Identity management for members.
- **orders & order_items**: Transactional tables tracking sales history.
- **reviews**: Customer feedback, restricted to one review per book per customer.
- **events & registrations**: Community engagement tracking.

## 🔍 Key Query Patterns

The project explores several critical SQL patterns:

### 1. The Search Filter
Uses `ILIKE` for case-insensitive partial matching across multiple joined tables:
```sql
SELECT b.title, a.last_name FROM books b
JOIN authors a ON b.author_id = a.id
WHERE b.title ILIKE '%search%' OR a.last_name ILIKE '%search%';
```

### 2. Verified Reviews
Enforces that a user can only review what they have actually purchased:
```sql
SELECT DISTINCT b.id, b.title FROM books b
JOIN order_items oi ON b.id = oi.book_id
JOIN orders o ON oi.order_id = o.id
WHERE o.customer_id = $1;
```

### 3. Inventory Control
Calculates current stock levels and handles restocking via `UPDATE` increments.

## 🎨 Visual Identity
The project follows the "Stockholm Minimalist" design system:
- **Primary**: #4A90E2 (Sky Blue)
- **Secondary**: #50E3C2 (Teal)
- **Accent**: #F5A623 (Amber)
- **Background**: #F8F8F8
- **Typography**: Clean monospace for a "modern technical" feel.

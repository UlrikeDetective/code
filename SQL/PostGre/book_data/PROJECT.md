# Project Specification: Database Learning Journey

This document outlines the architectural decisions and learning milestones achieved during the development of the Stockholm Bookshop project.

## 🎯 Learning Objectives

- **Relational Design**: Transitioning from "flat" data (CSV-style) to a normalized schema (3NF).
- **Advanced SQL**: Practicing Joins (INNER, LEFT), Aggregations (COUNT, SUM, AVG), and complex filtering (ILIKE, CASE).
- **Session Management**: Implementing stateful user experiences with `express-session`.
- **Financial Intelligence**: Modeling real-world business costs (fixed vs. variable) and visualizing break-even points.
- **Business Intelligence**: Building dashboards using SQL aggregations to identify best sellers, churn risks, and inventory needs.
- **CRUD Operations**: Full implementation of store management and customer interactions.
- **Transaction Logic**: Atomic handling of purchases impacting inventory and sales history.

## 🏗 Database Architecture

The project uses a normalized schema to ensure data integrity:

- **authors**: Biographical data.
- **genres**: Book categorization.
- **books**: The central inventory hub.
- **customers**: Identity and session tracking.
- **orders & order_items**: Transactional truth.
- **reviews**: Social feedback, restricted to one per book per customer.
- **events & registrations**: Community engagement metrics.

## 🔍 Key Intelligence Patterns

The project explores several critical business query patterns:

### 1. The BI Dashboard (Admin)
Aggregates sales data to find the top 5 performers and identify inactive customers:
```sql
SELECT c.first_name, SUM(o.total_amount) as total_spent
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.id ORDER BY total_spent DESC LIMIT 5;
```

### 2. User Feedback Loop
Automatically identifies purchased items in the catalog to provide "OWNED" status markers and verified review forms.

### 3. Inventory Health
Real-time tracking of zero-stock items and non-selling inventory to guide restocking decisions.

### 4. Financial P&L Modeling
A dedicated dashboard (`/admin/financials`) that simulates a Spanish business model ("Librería de Tarifa").
- **Cost Structure**: Hardcoded fixed costs (Rent, Staff, Social Security, Autónomo).
- **Revenue Streams**: Real-time aggregation of book sales (margin ~35%) and event tickets.
- **Break-Even Analysis**: Dynamic calculation of required sales volume to cover monthly burn.

## 🎨 Visual Identity
The project follows the "Stockholm Minimalist" design system:
- **Primary**: #4A90E2 (Sky Blue)
- **Secondary**: #50E3C2 (Teal)
- **Accent**: #F5A623 (Amber)
- **Background**: #F8F8F8
- **UI Logic**: Dynamic dashboards, session-aware headers, and clean monospace typography.

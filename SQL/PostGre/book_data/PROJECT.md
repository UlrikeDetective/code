# Project Specification: High Tide Books - Database Journey

This document outlines the architectural decisions and learning milestones achieved during the development of the High Tide Books project.

## 🎯 Learning Objectives

- **Relational Design**: Transitioning from "flat" data (CSV-style) to a normalized schema (3NF).
- **Advanced SQL**: Practicing Joins, Aggregations, Subqueries, and complex filtering (ILIKE, CASE).
- **Session Management**: Implementing stateful user experiences with `express-session`.
- **Financial Intelligence**: Modeling real-world business costs (fixed vs. variable) and visualizing break-even points.
- **Business Intelligence**: Building dashboards using SQL aggregations to identify best sellers, churn risks, and inventory needs.
- **Recommendation Engine**: Implementing hashtag similarity and collaborative filtering to predict customer interests.
- **CRUD Operations**: Full implementation of store management and customer interactions.
- **Transaction Logic**: Atomic handling of purchases impacting inventory and sales history.

## 🏗 Database Architecture

The project uses a normalized schema to ensure data integrity:

- **authors**: Biographical data.
- **genres**: Book categorization.
- **books**: The central inventory hub, featuring hashtags for search and discovery.
- **customers**: Identity and session tracking.
- **orders & order_items**: Transactional truth.
- **reviews**: Social feedback, restricted to one per book per customer.
- **events & registrations**: Community engagement metrics.

## 🔍 Key Intelligence Patterns

The project explores several critical business query patterns:

### 1. The Recommendation Engine
Suggests books based on two distinct patterns:
- **Hashtag Similarity**: Finds unpurchased books that share hashtags with a customer's existing library.
- **Collaborative Filtering**: Suggests books popular among other customers who bought similar items.

### 2. User Feedback Loop
Automatically identifies purchased items in the catalog to provide "OWNED" status markers and verified review forms.

### 3. Inventory & Event Tracking
- **Inventory Filter**: The public shop automatically filters out zero-stock items to prevent "ghost" sales.
- **Event Booking Status**: Session-aware UI identifies already-booked events to prevent double-registration.

### 4. Financial P&L Modeling
A dedicated dashboard (`/admin/financials`) that tracks real-time sales against fixed costs.
- **Cost Structure**: Monthly burn (Rent, Staff, Social Security, Autónomo).
- **Revenue Streams**: Real-time aggregation of book sales (margin ~35%) and event tickets.
- **Break-Even Analysis**: Dynamic calculation of required sales volume to cover monthly expenses.

## 🎨 Visual Identity
The project follows the "Stockholm Minimalist" design system:
- **Primary**: #4A90E2 (Sky Blue)
- **Secondary**: #50E3C2 (Teal)
- **Accent**: #F5A623 (Amber)
- **Background**: #F8F8F8
- **UI Logic**: Searchable autocomplete fields, dynamic dashboards, and clean monospace typography.

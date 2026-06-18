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

## 📅 Event Strategy: Summer of 2026

To foster community engagement, the shop hosts 5-6 events per week throughout July and August 2026.

### Event Types & Themes
- **The Lineup (Surf Club)**: Focused on ocean culture, sustainability, and surf technique.
- **Silicon Shores (Tech Club)**: Discussions on AI, digital nomadism, and the future of work.
- **Wanderlust Wayfarers (Travel Club)**: Highlighting hidden gems and slow travel.
- **Zen Kitchen (Cooking Club)**: Hands-on workshops in 'the bookshop kitchen' focusing on coastal and Japanese recipes.
- **Book Circle**: Deep dives into curated titles from the High Tide collection.

### Scheduling Rules
- **Frequency**: 5-6 days per week (Monday - Saturday).
- **Sunday**: No events (Store closed for staff surfing).
- **Locations**:
    - `the bookshop`: Main indoor area for book circles and tech talks.
    - `the bookshop veranda`: Outdoor area for travel tales and surf clubs.
    - `the bookshop kitchen`: Dedicated space for all Zen Kitchen events.
- **Rotation**: A balanced mix of themes ensuring no more than one event per day.
- **Time**: Default evening slot at 18:00; select workshops on Saturday mornings at 10:00.

### Summer 2026 Milestones
- **July**: Focus on "Japanese Culture & Tech" (aligning with Tokyo titles).
- **August**: Focus on "Atlantic Surfing & Coastal Living" (aligning with Hawaii and California titles).
A dedicated dashboard (`/admin/financials`) that tracks real-time sales against fixed costs stored in the `business_costs` table.
- **Cost Structure**: Monthly burn (Rent, Staff increasing to 3 Helpers @ 600€ as of June 2026, Social Security 32%, Autónomo).
- **Revenue Streams**: Real-time aggregation of book sales (margin ~35%) and event tickets.
- **Break-Even Analysis**: Dynamic calculation of required sales volume to cover monthly expenses.

## 🎨 Visual Identity
The project follows a "Surfer Wellness" design system, moving away from minimalist whites to organic, earthy tones:
- **Background**: #BED0D0 (Sage)
- **Primary**: #01393D (Deep Teal)
- **Secondary**: #56989F (Seafoam)
- **Accent**: #B77651 (Warm Ochre)
- **Text**: #6F452D (Rust)
- **UI Logic**: CSS-only graphics (surfboards, cacti, palms), searchable autocomplete, and a persistent Shopping Bag system.

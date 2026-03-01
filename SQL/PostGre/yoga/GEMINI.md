# Yoga Studio Management System (Tarifa Beach Yoga)

## Project Overview
This project is a full-stack web application designed for a yoga business in Tarifa. It handles student bookings for beach yoga lessons and provides the business owner with financial tracking and management tools.

### Key Features
*   **Student Interface:** Booking for solo yoga lessons or multi-class packages.
*   **Monthly Calendar:** Dynamic view of all scheduled lessons for 2026.
*   **Business Management (Owner Dashboard):**
    *   **Attendance Tracking:** Manage a database of residents/locals and visitors.
    *   **Package Management:** Track class credit balances for purchased packages.
    *   **Financial Tracking:** Monitor income from classes and expenses (gas, car, advertising, taxes).
    *   **Inventory Management:** Track yoga mat purchases and lifespans.

### Tech Stack
*   **Framework:** Django (Python)
*   **Database:** PostgreSQL
*   **Environment:** Conda (`django` environment)
*   **Configuration:** `.env` for secure credential management

---

## Building and Running

### 1. Environment Setup (COMPLETED)
The Conda environment `django` is active:
```bash
conda activate django
```

### 2. Dependency Installation (COMPLETED)
Required packages are installed: `django`, `psycopg2-binary`, `python-dotenv`, `django-environ`.

### 3. Database & Initial Setup (COMPLETED)
1.  **Configure `.env`:** Database `yoga` is created; `.env` is set up with all required variables.
2.  **Migrations:** [DONE] Database schema initialized with `python manage.py migrate`.
3.  **Seed Data:** [DONE] 2026 lessons generated.

### 4. Running the Project
```bash
python manage.py runserver
```

---

## Development Conventions

### Coding Style
*   **Python:** Adhere strictly to **PEP 8** style guidelines.
*   **Documentation:** All functions and classes are properly commented.
*   **Database:** Django Models enforce constraints (e.g., max 20 students, min 3 per lesson).

## Business Scenario
**Side Job:** Giving almost daily morning yoga lessons on the beach (beach = free) in Tarifa. If the weather is good, there are six yoga lessons per week (Monday to Saturday) between 9:00 AM and 10:00 AM. Occasionally, there is an extra lesson on Sunday or in the afternoon. At each lesson, there should be at least 3 students with a maximum of 20.

**Customer Segmentation:**
- **Local Residents:** Drop by regularly (mostly once per week).
- **Visitors:** Stay from a few days up to two weeks. Some return annually or multiple times a year.

**Marketing:** Advertising is done via blackboards at surf schools and cafes, and through Instagram ads.

## Business Rules & Costs (Implemented in Models)

### Lesson Packages (Income)
- **Single Lesson:** 15.00 €
- **3 Lessons:** 40.00 €
- **5 Lessons:** 50.00 €
- **10 Lessons:** 100.00 €

### Expense Structures
- **Yoga Mats (Inventory):**
    - 10 mats: 31.33 € / piece
    - 20 mats: 31.05 € / piece
    - 30 mats: 29.33 € / piece
    - *Note: Daily beach use gives a mat lifespan of 1-2 years.*
- **Recurring Costs:** Gas, Car maintenance, Taxes, and Advertising.

### Scheduling
- Standard morning sessions: Mon-Sat, 9:00 AM - 10:00 AM.
- Minimum 3 students / Maximum 20 students.


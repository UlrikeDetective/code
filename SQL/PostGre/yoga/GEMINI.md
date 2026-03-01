# Yoga Studio Management System (Tarifa Beach Yoga)

## Project Overview
This project is a full-stack web application designed for a yoga business in Tarifa. It handles student bookings for beach yoga lessons and provides the business owner with financial tracking and management tools.

### Key Features
*   **Student Interface:** Booking for solo yoga lessons or multi-class packages.
*   **Business Management (Owner Dashboard):**
    *   **Attendance Tracking:** Manage a database of residents/locals and visitors.
    *   **Package Management:** Track class credit balances for purchased packages.
    *   **Financial Tracking:** Monitor income from classes and expenses (gas, car, advertising, taxes).
    *   **Inventory Management:** Track yoga mat purchases and lifespans (1-2 years).

### Tech Stack
*   **Framework:** Django (Python)
*   **Database:** PostgreSQL
*   **Environment:** Conda
*   **Configuration:** `.env` for secure credential management

---

## Building and Running

### 1. Environment Setup
Create and activate the Conda environment:
```bash
conda create -n yoga python=3.12
conda activate yoga
```

### 2. Dependency Installation
```bash
pip install django psycopg2-binary python-dotenv django-environ
```

### 3. Database & Initial Setup
1.  Configure `.env` with `DATABASE_URL`, `SECRET_KEY`, and `DEBUG` mode.
2.  Initialize the Django project:
```bash
django-admin startproject yoga_project .
python manage.py startapp core
```
3.  Run migrations:
```bash
python manage.py migrate
```

### 4. Running the Project
```bash
python manage.py runserver
```

---

## Development Conventions

### Coding Style
*   **Python:** Adhere strictly to **PEP 8** style guidelines.
*   **Documentation:** All functions and classes must be properly commented.
*   **Database:** Use Django Models to enforce constraints (e.g., max 20 students, min 3 per lesson).

### Business Rules
*   **Pricing:**
    *   Single: 15€
    *   3 Lessons: 40€
    *   5 Classes: 50€
    *   10 Classes: 100€
*   **Mat Inventory Pricing:**
    *   10 mats: 31.33€/ea
    *   20 mats: 31.05€/ea
    *   30 mats: 29.33€/ea
*   **Scheduling:** Standard morning sessions (Mon-Sat, 9am-10am).

### Security
*   Never commit `.env` or any sensitive credentials.
*   Use `django-environ` to handle sensitive settings.

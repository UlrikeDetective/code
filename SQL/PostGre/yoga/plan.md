# Strategic Plan: Yoga Studio Management System

## 1. Understanding the Goal
The objective is to build a full-stack web application for a beach yoga business in Tarifa using **Django** and **PostgreSQL**. The system will manage student bookings (front end) and business operations/analytics (back end).

## 2. Business Financial Parameters
Based on the project requirements, the system must hardcode or allow configuration of the following:

### Income (Lesson Packages)
*   **Single Lesson:** 15.00 €
*   **3 Lessons:** 40.00 €
*   **5 Lessons:** 50.00 €
*   **10 Lessons:** 100.00 €

### Expenses (Cost of Doing Business)
*   **Yoga Mats (Inventory):**
    *   10 mats: 31.33 € / piece
    *   20 mats: 31.05 € / piece
    *   30 mats: 29.33 € / piece
    *   *Note: Lifetime of 1-2 years for beach use.*
*   **Recurring Costs:** Gas, Car maintenance, Taxes.
*   **Advertising:** Blackboards at surf schools/cafes, Instagram ads, and other marketing.

## 3. Investigation & Analysis
### Current Environment
*   **OS:** Darwin (macOS).
*   **Stack:** Python (Django), PostgreSQL, Conda (Environment management), `.env` (Security).
*   **Constraints:** Max 20 students, Min 3 students per lesson. Standard time: Mon-Sat 9am-10am.

### Critical Implementation Questions
*   **Payment Tracking:** Will the system record manual payments (Cash/Bizum) or integrate a provider like Stripe? *Initial plan: Manual recording with digital readiness.*
*   **Customer Segmentation:** Need to distinguish between "Locals" (regulars) and "Visitors" (temporary/seasonal) for marketing analytics.

## 4. Proposed Strategic Approach

### Phase 1: Environment & Project Setup
1.  **Conda Setup:** Create a dedicated environment (`conda create -n yoga python=3.12`).
2.  **Django Init:** Install `django`, `psycopg2-binary`, `python-dotenv`.
3.  **Database Configuration:** Set up PostgreSQL and link via `.env` to keep credentials secure.

### Phase 2: Data Modeling (The Backend Core)
Define the following models in Django:
*   **`Customer`**: Tracks name, email, and "Local vs. Visitor" status.
*   **`Lesson`**: Date/time, status (Scheduled/Completed), and attendee list.
*   **`Package`**: Tracks purchased credits (e.g., a "10-pack") and remaining balance.
*   **`Expense`**: Categorized logs for **Taxes, Gas, Advertising, and Mat purchases**.
*   **`Inventory`**: Specifically tracks Mat lifespan and replacement alerts.

### Phase 3: Business Logic & Dashboards
1.  **Booking Logic:** Automate credit deduction. Block bookings once 20 spots are filled.
2.  **Financial Reporting:** Create an owner-only view calculating:
    *   **Gross Income** (Package sales).
    *   **Net Profit** (Income minus Taxes, Gas, Ads, and Mat depreciation).
    *   **Weekly/Monthly/Yearly Trends.**

### Phase 4: Frontend Development
1.  **Public Site:** Responsive booking calendar for students.
2.  **Owner Dashboard:** A "Beach Mode" interface optimized for mobile use on the sand (quick attendance marking and expense logging).

## 5. Verification Strategy
*   **Credit Validation:** Ensure that booking a lesson correctly reduces the student's package balance.
*   **Financial Audit:** Test that adding a 20-mat purchase at 31.05€ correctly updates the expense reports.
*   **Capacity Check:** Verify that the 21st student is placed on a waitlist or blocked.

## 6. Anticipated Challenges & Considerations
*   **Mobile-First Design:** The owner will use this on a phone at the beach; UI must be simple and high-contrast.
*   **Weather Dependency:** Lessons depend on good weather. The system needs a "Bulk Cancel & Notify" feature for windy or rainy days.
*   **Data Persistence:** Ensure Postgres is configured for daily backups of financial records.

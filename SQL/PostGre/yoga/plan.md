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
1.  **Conda Setup:** use conda activate django.
2.  **Django Init:** Install `django`, `psycopg2-binary`, `python-dotenv`. - already installed
3.  **Database Configuration:** Set up PostgreSQL and link via `.env` to keep credentials secure. - already created database "yoga" and set-up .env.

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

## 7. color theme

* Theme: Wind, Whitewash, and the Strait.
* This palette captures the stark white walls of the old town, the golden shifting dunes of Valdevaqueros, and the deep, swirling blues where two seas collide.
*  Pueblo Blanco #FFFFFF (Crisp Lime-Wash), #F2F2F2 (Salt Spray), #D1CCC0 (Ancient Cobblestone)
*  The Two Seas #005F73 (Deep Atlantic), #0A9396 (Mediterranean Teal), #94D2BD 
(Shallow Lagoon)
* The Dunes #E9D8A6 (Windblown Sand), #EE9B00 (Golden Hour Sun), #CA6702 (Terra Cotta Roofs)
* Levante Energy #AE2012 (Spanish Red), #3D5A80 (Kitesurf Blue), #001219 (The Strait at Night)

## 8. Font style
1. The "Nautical Log" (IBM Plex Mono)
This is a high-precision, modern monospace font. It feels like a technical readout for wind speeds or a ship’s GPS. It balances the "high-tech" kiteboarding scene with the ruggedness of the Atlantic.
Vibe: Professional, clean, and rhythmic.
Best for: Clean website layouts or minimalist branding.

2. The "Sun-Bleached Postcard" (Courier Prime)
Unlike the standard Courier you find on old Windows PCs, Courier Prime was redesigned for screen legibility while keeping the authentic typewriter soul. It captures the "Pueblo Blanco" (White Village) aesthetic—simple, honest, and timeless.
Vibe: Nostalgic, literary, and relaxed.
Best for: Long-form body text or personal travel blogs.

3. The "Salt-Sprayed Journal" (Special Elite)
If you want something that looks like an old typewriter that’s been sitting in a seaside cafe for 30 years, this is it. It has a slightly "gritty" ink-bleed effect that mimics the weathered texture of the Castillo de Guzmán el Bueno.
Vibe: Rugged, bohemian, and authentic.
Best for: Headlines, quotes, or social media graphics.

4. The "Surf Culture" (Space Mono)
This font is eclectic and geometric. It has a "futuristic-retro" feel that matches the high-energy, colorful sails of the kitesurfers at Valdevaqueros. It’s quirky, just like Tarifa’s narrow, winding streets.
Vibe: Eclectic, modern, and high-energy.
Best for: Bold headers or call-to-action buttons.

Pairing: Vintage/Boho Look Headline: Special Elite Sub-header: Courier Prime (Italic)Body Text: Courier Prime or
Modern/Technical Look Headline: Space Mono (Bold) Sub-header: IBM Plex Mono Body Text: Roboto Mono
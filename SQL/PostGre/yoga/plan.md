# Strategic Plan: Yoga Studio Management System (Tarifa Beach Yoga)

## 0. Project Description
**Tarifa Beach Yoga** is a full-stack management system designed for a boutique side-business offering morning yoga sessions on the sun-bleached shores of Tarifa. The application serves two primary purposes: providing a seamless, "Zen" booking experience for students (both local residents and seasonal visitors) and a robust "Beach Mode" dashboard for the owner to manage finances, inventory, and attendance under the bright Andalusian sun.

The project is a learning-focused implementation using **Django** and **PostgreSQL**, prioritizing functional business logic and a high-contrast, mobile-first aesthetic inspired by the "Pueblo Blanco" and the swirling blues of the Strait.

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

## 4. Proposed Strategic Approach

### Phase 1: Environment & Project Setup [COMPLETED]
1.  **Conda Setup:** [DONE] Created and activated `django` environment.
2.  **Django Dependencies:** [DONE] Installed `django`, `psycopg2-binary`, `python-dotenv`.
3.  **Database Configuration:** [DONE] Created `yoga` database and configured `.env`.
4.  **Django Initialization:** [DONE] Initialized project `yoga_project` and app `core`.

### Phase 2: Data Modeling [COMPLETED]
1.  **Models Defined:** [DONE] `Customer`, `Lesson`, `Package`, `Expense`, and `Inventory` models implemented.
2.  **Migrations:** [DONE] Database schema applied to PostgreSQL.
3.  **Admin Registration:** [DONE] All models registered for easy management.

### Phase 3: Business Logic & Dashboards [COMPLETED]
1.  **Booking Logic:** [DONE] Credit deduction, session-based login, and capacity blocking.
2.  **Financial Reporting:** [DONE] Owner view with gross income, expenses, and profit.
3.  **Advanced Tracking:** [DONE] "Active Tarifa Locals" monitoring for local engagement.
4.  **Seed Data:** [DONE] 2026 schedule created.

### Phase 4: Frontend Development [COMPLETED]
1.  **Design Theme:** [DONE] "Wind, Whitewash, and the Strait" with 🪷 Lotus iconography.
2.  **Monthly Calendar:** [DONE] Navigation, booked highlights, and real-time spot counts.
3.  **Owner Dashboard:** [DONE] Three-column grid with attendance and local tracking.
4.  **Public Booking:** [DONE] Smooth flow with session persistence and "Balance Check" feature.

## 7. Color Theme (Implemented)
* **Theme:** Wind, Whitewash, and the Strait.
* This palette captures the stark white walls of the old town, the golden shifting dunes of Valdevaqueros, and the deep, swirling blues where two seas collide.
* **Pueblo Blanco:** #FFFFFF (Crisp Lime-Wash), #F2F2F2 (Salt Spray), #D1CCC0 (Ancient Cobblestone)
* **The Two Seas:** #005F73 (Deep Atlantic), #0A9396 (Mediterranean Teal), #94D2BD (Shallow Lagoon)
* **The Dunes:** #E9D8A6 (Windblown Sand), #EE9B00 (Golden Hour Sun), #CA6702 (Terra Cotta Roofs)
* **Levante Energy:** #AE2012 (Spanish Red), #3D5A80 (Kitesurf Blue), #001219 (The Strait at Night)

## 8. Font Style (Implemented)
1. **The "Nautical Log" (IBM Plex Mono)**
   * High-precision, modern monospace font. Feels like a technical readout for wind speeds.
   * Vibe: Professional, clean, and rhythmic.
2. **The "Sun-Bleached Postcard" (Courier Prime)**
   * Redesigned for screen legibility while keeping the authentic typewriter soul.
   * Vibe: Nostalgic, literary, and relaxed.
3. **The "Salt-Sprayed Journal" (Special Elite)**
   * Looks like an old typewriter sitting in a seaside cafe for 30 years.
   * Vibe: Rugged, bohemian, and authentic.
4. **The "Surf Culture" (Space Mono)**
   * Eclectic and geometric. Matches the high-energy kitesurfers at Valdevaqueros.
   * Vibe: Eclectic, modern, and high-energy.

**Implementation Pairing:**
* **Headline:** Space Mono (Bold)
* **Body Text:** IBM Plex Mono

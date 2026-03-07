# Lesson Management Guide (Tarifa Beach Yoga)

As the admin of the Yoga Studio Management System, you can manage your daily lessons (adding new ones, cancelling existing ones, or marking attendance) through the **Django Admin Interface**.

## 1. Accessing the Admin Interface
1. Ensure your server is running (`python manage.py runserver`).
2. Open your browser and go to: `http://localhost:8000/admin/`
3. Log in with your superuser credentials.
   * *If you haven't created one yet, run: `conda run -n django python manage.py createsuperuser`*

## 2. Managing Lessons

### Adding a New Lesson
*   Navigate to **Core > Lessons** and click **"Add Lesson"**.
*   Select the **Date** and **Time** (standard is 09:00).
*   Specify **Max Students** (default 20) and **Min Students** (default 3).
*   Click **Save**. The new lesson will immediately appear on the public calendar.

### Cancelling a Lesson (e.g., due to Levante wind)
*   Navigate to **Core > Lessons** and find the specific date.
*   Open the lesson and check the **"Is cancelled"** box.
*   Add a reason in the **Notes** section (e.g., "Too windy - Levante").
*   Click **Save**. The lesson will appear as "Struck-through" on the calendar for students to see.

### Marking Attendance (Beach Mode)
*   Instead of navigating through the admin menu, use the **Owner Dashboard**.
*   All lessons scheduled for today will appear in the **"Today's Lessons"** section.
*   Click the **"Mark Attendance"** button next to the lesson. This opens a dedicated attendance page with a list of all booked students.
*   Once you've verified everyone is present, click **"Confirm All Present"**.

### Managing Cancellations (24h Rule)
*   The system allows students to cancel their own bookings directly from the lesson page.
*   **The 24-hour rule:** Cancellations are only permitted more than 24 hours before the lesson starts. 
*   If a student cancels in time, 1 lesson is automatically added back to their package balance.
*   Within 24 hours of the lesson, the "Cancel" button is disabled, and the credit is not refunded.

### Tracking Local Engagement
*   The **"Tarifa Locals: Last Booking"** section shows you all students from Tarifa and the date of their furthest booked lesson in 2026. This helps you see how far into the future your most loyal students have already planned their practice.

## 3. Managing Packages & Expenses
*   **Packages:** When a customer buys a 10-pack, add it under **Core > Packages**. The system will track the remaining lessons.
*   **Expenses:** Log your gas, car maintenance, or new yoga mat purchases under **Core > Expenses**.
*   **Tax Compliance:** Use the dashboard's **Monthly Financial Overview** to see your profit after **IVA (21%)**, **IRPF (20%)**, and **Social Security (RETA)**. Log your Social Security payments as expenses with the category **"Social Security"** to ensure they are deducted from your net profit.

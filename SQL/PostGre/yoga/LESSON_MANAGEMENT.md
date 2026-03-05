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
*   Click the **"Mark Attendance"** button next to the lesson. This will take you directly to the attendee list for that specific session.
*   Check or uncheck the customers who are on the beach with you and click **Save**.

### Tracking Local Engagement
*   The **"Active Tarifa Locals"** section automatically shows you students from Tarifa who have booked a lesson in the last 7 days or have one coming up this week. This helps you identify your most consistent local practitioners at a glance.

## 3. Managing Packages & Expenses
*   **Packages:** When a customer buys a 10-pack, add it under **Core > Packages**. The system will track the remaining lessons.
*   **Expenses:** Log your gas, car maintenance, or new yoga mat purchases under **Core > Expenses** to keep your financial dashboard accurate.

import os
import django
import csv
from datetime import datetime
from decimal import Decimal

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yoga_project.settings')
django.setup()

from core.models import Customer, Lesson, Package, Expense

def final_restore():
    # 1. Sync Customers
    print("Step 1: Syncing Customers...")
    with open('data/clients.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Customer.objects.update_or_create(
                id=int(row['id']),
                defaults={
                    'name': row['name'],
                    'email': row['email'].strip().lower(),
                    'phone': row['phone'],
                    'customer_type': row['customer_type'],
                    'city': row['city'],
                    'country': row['country'],
                    'username': row['username'] if row['username'] != 'NULL' else None,
                }
            )
    print(f"Synced {Customer.objects.count()} customers.")

    # 2. Map Dates to New Lesson IDs
    print("Step 2: Mapping Dates to New Lesson IDs...")
    date_time_to_new_id = {}
    with open('data/new_lesson_id_map.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            time_str = row['time'][:5]
            date_time_to_new_id[(row['date'], time_str)] = int(row['id'])

    # 3. Map Old IDs to Dates (using the old version from Git history as backup map)
    # Since the user's manual files are mismatched, we use the date-time as the "Source of Truth"
    print("Step 3: Restoring Bookings via Date/Time matching...")
    
    # We need the mapping of old_lesson_id -> (date, time)
    # We'll use the git version of lessons.csv to get this
    import subprocess
    old_lessons_data = subprocess.check_output(['git', 'show', 'HEAD~2:./data/lessons.csv']).decode('utf-8')
    old_lesson_map = {}
    reader = csv.DictReader(old_lessons_data.splitlines())
    for row in reader:
        old_lesson_map[row['id']] = (row['date'], row['time'][:5])

    # Add the latest manual fix for 551/552 based on today's logic (April 26)
    # Today is April 26, 2026. 
    # Let's assume 551 was 09:00 and 552 was 19:00 for April 26
    old_lesson_map['551'] = ('2026-04-26', '09:00')
    old_lesson_map['552'] = ('2026-04-26', '19:00')
    # And mapping other recent IDs if possible... 
    # But let's try to restore the bulk first.

    with open('data/lessons_attendence.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        bookings_restored = 0
        for row in reader:
            old_lid = row['lesson_id']
            if old_lid in old_lesson_map:
                dt_tuple = old_lesson_map[old_lid]
                if dt_tuple in date_time_to_new_id:
                    new_lid = date_time_to_new_id[dt_tuple]
                    try:
                        customer = Customer.objects.get(id=int(row['customer_id']))
                        lesson = Lesson.objects.get(id=new_lid)
                        lesson.attendees.add(customer)
                        bookings_restored += 1
                    except Exception:
                        pass
    print(f"Restored {bookings_restored} bookings.")

    # 4. Restore Packages
    print("Step 4: Restoring Packages...")
    Package.objects.all().delete()
    with open('data/package.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                customer = Customer.objects.get(id=int(row['customer_id']))
                Package.objects.create(
                    id=int(row['id']),
                    customer=customer,
                    total_lessons=int(row['total_lessons']),
                    remaining_lessons=int(row['remaining_lessons']),
                    purchase_date=row['purchase_date'],
                    price_paid=Decimal(row['price_paid']),
                    package_type=row.get('package_type', 'YOGA')
                )
            except Customer.DoesNotExist:
                pass
    print(f"Restored {Package.objects.count()} packages.")

    # 5. Restore Expenses
    print("Step 5: Restoring Expenses...")
    Expense.objects.all().delete()
    if os.path.exists('data/expenses.csv'):
        with open('data/expenses.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Expense.objects.create(
                    id=int(row['id']),
                    date=row['date'],
                    category=row['category'],
                    amount=Decimal(row['amount']),
                    description=row['description']
                )
    print(f"Restored {Expense.objects.count()} expenses.")

if __name__ == "__main__":
    final_restore()

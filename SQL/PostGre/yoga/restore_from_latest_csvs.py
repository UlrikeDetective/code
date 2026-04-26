import os
import django
import csv
from datetime import datetime
from decimal import Decimal

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yoga_project.settings')
django.setup()

from core.models import Customer, Lesson, Package, Expense

def restore_from_latest_csvs():
    # 1. Sync Customers (can be re-run, should be idempotent)
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

    # 2. Import Lessons from data/lessons.csv
    print("Step 2: Importing Lessons from data/lessons.csv...")
    Lesson.objects.all().delete()
    with open('data/lessons.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        lessons_imported = 0
        for row in reader:
            try:
                Lesson.objects.create(
                    id=int(row['id']),
                    date=row['date'],
                    time=row['time'],
                    max_students=int(row['max_students']),
                    min_students=int(row['min_students']),
                    is_cancelled=row['is_cancelled'].lower() == 'true',
                    notes=row['notes'],
                    lesson_type=row.get('lesson_type', 'YOGA') # Default to YOGA if missing
                )
                lessons_imported += 1
            except Exception as e:
                print(f"Error importing lesson ID {row.get('id', 'N/A')}: {e}")
    print(f"Imported {lessons_imported} lessons.")

    # 3. Restore Packages
    print("Step 3: Restoring Packages...")
    Package.objects.all().delete()
    with open('data/package.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        packages_imported = 0
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
                    package_type=row.get('package_type', 'YOGA') # Default to YOGA if missing
                )
                packages_imported += 1
            except Customer.DoesNotExist:
                print(f"Warning: Customer ID {row['customer_id']} not found for package ID {row['id']}.")
            except Exception as e:
                print(f"Error importing package ID {row.get('id', 'N/A')}: {e}")
    print(f"Restored {packages_imported} packages.")

    # 4. Restore Bookings (from empty file or unmappable IDs)
    print("Step 4: Restoring Bookings...")
    bookings_restored = 0
    # Attempting to restore from lessens_attendence_2026_04_10.csv (which is empty)
    if os.path.exists('data/lessens_attendence_2026_04_10.csv'):
        with open('data/lessens_attendence_2026_04_10.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader: # This loop will not run if the file is empty
                try:
                    customer = Customer.objects.get(id=int(row['customer_id']))
                    # The lesson_id from attendance is old and doesn't match current lesson IDs
                    # So, Lesson.objects.get(id=int(row['lesson_id'])) will fail.
                    # We are intentionally ignoring these IDs as per user request.
                    pass
                except Exception: pass
    
    # If the user meant to use the current lessons_attendence.csv, it has old IDs that don't map.
    # If they meant the empty file, no bookings are restored.
    # Thus, bookings_restored will remain 0.
    print(f"Restored {bookings_restored} bookings. (As expected due to ID mismatch or empty file).")

    # 5. Restore Expenses
    print("Step 5: Restoring Expenses...")
    Expense.objects.all().delete()
    if os.path.exists('data/expenses.csv'):
        with open('data/expenses.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            expenses_imported = 0
            for row in reader:
                try:
                    Expense.objects.create(
                        id=int(row['id']),
                        date=row['date'],
                        category=row['category'],
                        amount=Decimal(row['amount']),
                        description=row['description']
                    )
                    expenses_imported += 1
                except Exception as e:
                    print(f"Error importing expense ID {row.get('id', 'N/A')}: {e}")
    print(f"Restored {expenses_imported} expenses.")

if __name__ == "__main__":
    restore_from_latest_csvs()

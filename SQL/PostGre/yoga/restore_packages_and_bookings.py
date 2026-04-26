import os
import django
import csv
from datetime import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yoga_project.settings')
django.setup()

from core.models import Customer, Lesson, Package

def restore_data():
    # 1. Restore Packages
    package_csv = 'data/package.csv'
    if os.path.exists(package_csv):
        print("Restoring Packages...")
        with open(package_csv, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            packages_created = 0
            for row in reader:
                try:
                    customer = Customer.objects.get(id=int(row['customer_id']))
                    Package.objects.get_or_create(
                        id=int(row['id']),
                        defaults={
                            'customer': customer,
                            'total_lessons': int(row['total_lessons']),
                            'remaining_lessons': int(row['remaining_lessons']),
                            'purchase_date': row['purchase_date'],
                            'price_paid': row['price_paid'],
                            'package_type': 'YOGA'
                        }
                    )
                    packages_created += 1
                except Customer.DoesNotExist:
                    print(f"Customer {row['customer_id']} not found for package {row['id']}")
        print(f"Restored {packages_created} packages.")

    # 2. Map old lesson IDs to Date/Time
    lesson_map = {}
    lessons_csv = 'data/lessons.csv'
    if os.path.exists(lessons_csv):
        with open(lessons_csv, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Store as (date, time) tuple
                # CSV time is 09:00:00, Model default might be 09:00
                time_str = row['time'][:5] # Get HH:MM
                lesson_map[row['id']] = (row['date'], time_str)

    # 3. Restore Bookings
    attendance_csv = 'data/lessons_attendence.csv'
    if os.path.exists(attendance_csv):
        print("Restoring Bookings...")
        with open(attendance_csv, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            bookings_restored = 0
            for row in reader:
                old_lesson_id = row['lesson_id']
                customer_id = row['customer_id']
                
                if old_lesson_id in lesson_map:
                    date_val, time_val = lesson_map[old_lesson_id]
                    try:
                        customer = Customer.objects.get(id=int(customer_id))
                        # Find the new lesson instance
                        lesson = Lesson.objects.filter(date=date_val, time=time_val).first()
                        if lesson:
                            lesson.attendees.add(customer)
                            bookings_restored += 1
                        else:
                            # If lesson doesn't exist (e.g. it was a Sunday or special session not in seed)
                            # Create it as a Yoga lesson
                            lesson = Lesson.objects.create(
                                date=date_val,
                                time=time_val,
                                lesson_type='YOGA'
                            )
                            lesson.attendees.add(customer)
                            bookings_restored += 1
                    except Customer.DoesNotExist:
                        pass
        print(f"Restored {bookings_restored} bookings.")

if __name__ == "__main__":
    restore_data()

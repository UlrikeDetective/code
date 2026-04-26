import os
import django
import csv
from datetime import datetime
from decimal import Decimal

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yoga_project.settings')
django.setup()

from core.models import Customer, Lesson, Package, Expense

def restore_with_mapping(): # Corrected function name
    # 1. Sync Customers (idempotent)
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

    # 2. Import Lessons from latest data/lessons.csv
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
                    lesson_type=row.get('lesson_type', 'YOGA')
                )
                lessons_imported += 1
            except Exception as e:
                print(f"Error importing lesson ID {row.get('id', 'N/A')}: {e}")
    print(f"Imported {lessons_imported} lessons from data/lessons.csv.")

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
                    package_type=row.get('package_type', 'YOGA')
                )
                packages_imported += 1
            except Customer.DoesNotExist:
                print(f"Warning: Customer ID {row['customer_id']} not found for package ID {row.get('id', 'N/A')}.")
            except Exception as e:
                print(f"Error importing package ID {row.get('id', 'N/A')}: {e}")
    print(f"Restored {packages_imported} packages.")

    # 4. Restore Bookings using the mapping
    print("Step 4: Restoring Bookings...")
    
    # Map old lesson IDs to Date/Time from data/lessons_2026_03_27.csv
    old_id_to_dt = {}
    try:
        with open('data/lessons_2026_03_27.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                old_id_to_dt[row['id']] = (row['date'], row['time'][:5])
        print(f"Created mapping for {len(old_id_to_dt)} old lesson IDs from data/lessons_2026_03_27.csv.")
    except FileNotFoundError:
        print("Error: data/lessons_2026_03_27.csv not found. Cannot map old lesson IDs.")
        # Proceeding without old mapping, bookings might not restore

    # Map Date/Time to New Lesson IDs from latest data/lessons.csv
    dt_to_new_id = {}
    try:
        with open('data/lessons.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                dt_to_new_id[(row['date'], row['time'][:5])] = int(row['id'])
        print(f"Created mapping for {len(dt_to_new_id)} new lesson IDs from data/lessons.csv.")
    except FileNotFoundError:
        print("Error: data/lessons.csv not found. Cannot map to new lesson IDs.")
        return

    # Save mappings to CSV for inspection
    with open('old_lesson_id_map.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['old_id', 'date', 'time'])
        for old_id, (date, time) in old_id_to_dt.items():
            writer.writerow([old_id, date, time])
    print("Saved old lesson ID mapping to old_lesson_id_map.csv")

    with open('new_lesson_id_map.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['date', 'time', 'new_id'])
        for (date, time), new_id in dt_to_new_id.items():
            writer.writerow([date, time, new_id])
    print("Saved new lesson ID mapping to new_lesson_id_map.csv")

    # Restore Bookings from data/lessens_attendence_2026_04_10.csv
    bookings_restored = 0
    attendance_file = 'data/lessens_attendence_2026_04_10.csv'
    
    print(f"Checking attendance file: {attendance_file}")
    if os.path.exists(attendance_file) and os.path.getsize(attendance_file) > 0:
        print(f"Attendance file found and is not empty. Size: {os.path.getsize(attendance_file)} bytes.")
        with open(attendance_file, mode='r', encoding='utf-8') as f:
            try:
                reader = csv.DictReader(f)
                header = reader.fieldnames
                print(f"Attendance file header: {header}")
                
                if not header or 'lesson_id' not in header or 'customer_id' not in header:
                    print("Error: Attendance file is missing required columns ('lesson_id', 'customer_id').")
                else:
                    rows_processed = 0
                    for row in reader:
                        rows_processed += 1
                        old_lid = row.get('lesson_id')
                        cid = row.get('customer_id')

                        if not old_lid or not cid:
                            print(f"Skipping row due to missing 'lesson_id' or 'customer_id': {row}")
                            continue

                        print(f"Processing attendance row: old_lid={old_lid}, cid={cid}")
                        
                        if old_lid in old_id_to_dt:
                            dt_tuple = old_id_to_dt[old_lid]
                            print(f"  Old lesson ID {old_lid} maps to date/time: {dt_tuple}")
                            if dt_tuple in dt_to_new_id:
                                new_lid = dt_to_new_id[dt_tuple]
                                print(f"  Found new lesson ID {new_lid} for {dt_tuple}")
                                try:
                                    customer = Customer.objects.get(id=int(cid))
                                    lesson = Lesson.objects.get(id=new_lid)
                                    print(f"  Found Customer: {customer.name} (ID: {customer.id}), Lesson: {lesson} (ID: {lesson.id})")
                                    if not lesson.attendees.filter(id=customer.id).exists():
                                        lesson.attendees.add(customer)
                                        lesson.save() # Explicitly save after M2M add
                                        bookings_restored += 1
                                        print(f"  Successfully restored booking for customer {cid} to lesson {new_lid}.")
                                    else:
                                        print(f"  Customer {cid} already booked for lesson {new_lid}.")
                                except Customer.DoesNotExist:
                                    print(f"Skipping booking: Customer ID {cid} not found.")
                                except Lesson.DoesNotExist:
                                    print(f"Skipping booking: New lesson ID {new_lid} not found for date/time {dt_tuple}.")
                                except Exception as e:
                                    print(f"Skipping booking for customer {cid}, old lesson {old_lid} (new lesson {new_lid}): {e}")
                            else: 
                                print(f"No new lesson found for date/time {dt_tuple} corresponding to old lesson ID {old_lid}.")
                        else: 
                            print(f"Old lesson ID {old_lid} not found in mapping from data/lessons_2026_03_27.csv.")
                    print(f"Finished processing attendance file. Processed {rows_processed} rows.")
    else:
        print(f"Attendance file '{attendance_file}' not found or is empty. No bookings to restore from this file.")
                
    print(f"Restored {bookings_restored} bookings.")

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
    restore_with_mapping()

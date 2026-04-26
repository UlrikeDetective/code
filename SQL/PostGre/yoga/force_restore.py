import os
import django
import csv
from datetime import datetime
from decimal import Decimal

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yoga_project.settings')
django.setup()

from core.models import Customer, Lesson, Package, Expense

def force_restore():
    # 1. Map Today's IDs to Date/Time
    print("Mapping new Lesson IDs...")
    dt_to_new_id = {}
    with open('data/lesson_id_map_final.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dt_to_new_id[(row['date'], row['time'][:5])] = int(row['id'])

    # 2. Extract Old IDs from Git (HEAD~1)
    print("Mapping old Lesson IDs from Git...")
    import subprocess
    old_data = subprocess.check_output(['git', 'show', 'HEAD~1:./data/lessons.csv']).decode('utf-8')
    old_id_to_dt = {}
    reader = csv.DictReader(old_data.splitlines())
    for row in reader:
        # ID is first column, usually no quotes but DictReader handles it
        old_id_to_dt[row['id']] = (row['date'], row['time'][:5])

    # 3. Handle the "Missing" IDs (490, 551, 552, etc.)
    # Since we don't have the old lessons.csv for these, we have to look for patterns 
    # OR assume they follow the schedule. 
    # BUT wait! If lesson_id 490 exists in attendance, it MUST have existed in some db version.
    
    print("Processing Bookings...")
    with open('data/lessons_attendence.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        restored = 0
        missed_ids = set()
        
        for row in reader:
            old_lid = row['lesson_id']
            cid = row['customer_id']
            
            # Case A: Found in git map
            if old_lid in old_id_to_dt:
                dt = old_id_to_dt[old_lid]
                if dt in dt_to_new_id:
                    new_lid = dt_to_new_id[dt]
                    try:
                        customer = Customer.objects.get(id=int(cid))
                        lesson = Lesson.objects.get(id=new_lid)
                        lesson.attendees.add(customer)
                        restored += 1
                    except Exception: pass
            else:
                missed_ids.add(old_lid)

    print(f"Restored {restored} bookings from Git-mapped IDs.")
    print(f"Still missing mapping for {len(missed_ids)} IDs: {sorted(list(missed_ids))[:10]}...")

    # Case B: For the missing IDs, they might be in the current database already?
    # No, because we deleted them.
    
    # Let's try to restore packages as well
    print("Restoring Packages...")
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
            except Exception: pass
            
if __name__ == "__main__":
    force_restore()

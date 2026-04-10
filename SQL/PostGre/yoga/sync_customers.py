import os
import django
import csv
from datetime import datetime
from django.utils import timezone

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yoga_project.settings')
django.setup()

from core.models import Customer

def sync_customers():
    """
    Synchronizes the Customer table with data from data/clients.csv.
    """
    csv_file_path = 'data/clients.csv'
    
    if not os.path.exists(csv_file_path):
        print(f"Error: {csv_file_path} not found.")
        return

    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        count_updated = 0
        count_created = 0
        
        for row in reader:
            customer_id = int(row['id'])
            
            # Prepare defaults for update_or_create
            defaults = {
                'name': row['name'],
                'email': row['email'].strip().lower(),
                'phone': row['phone'],
                'customer_type': row['customer_type'],
                'city': row['city'],
                'country': row['country'],
                'username': row['username'] if row['username'] != 'NULL' else None,
            }
            
            # Try to get existing customer or create a new one
            customer, created = Customer.objects.update_or_create(
                id=customer_id,
                defaults=defaults
            )
            
            # Force update created_at if it's provided in CSV
            # Since auto_now_add=True might prevent initial set or update
            if row['created_at']:
                try:
                    # Parse the ISO format string
                    # Example: 2026-03-03 22:19:55.810569+01
                    # We might need to handle the timezone offset
                    created_at_dt = row['created_at']
                    Customer.objects.filter(id=customer_id).update(created_at=created_at_dt)
                except Exception as e:
                    print(f"Warning: Could not update created_at for ID {customer_id}: {e}")

            if created:
                count_created += 1
            else:
                count_updated += 1
                
        print(f"Synchronization complete.")
        print(f"Total customers processed: {count_created + count_updated}")
        print(f"New customers created: {count_created}")
        print(f"Existing customers updated: {count_updated}")

if __name__ == "__main__":
    sync_customers()

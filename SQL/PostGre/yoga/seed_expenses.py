import os
import django
from datetime import date
from decimal import Decimal

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yoga_project.settings')
django.setup()

from core.models import Expense

def seed_march_expenses():
    # Adding March 2026 Social Security & other expenses
    march_expenses = [
        {'date': date(2026, 4, 5), 'category': 'SOCIAL', 'amount': Decimal('230.00'), 'description': 'RETA Social Security April'},
        {'date': date(2026, 4, 10), 'category': 'ADS', 'amount': Decimal('45.00'), 'description': 'Instagram Ads - April Promo'},
        {'date': date(2026, 4, 15), 'category': 'GAS', 'amount': Decimal('30.00'), 'description': 'Gas to Tarifa Beach'},
        {'date': date(2026, 4, 20), 'category': 'INSURANCE', 'amount': Decimal('30.00'), 'description': 'Professional Liability Insurance (Monthly)'},
    ]
    
    for ex in march_expenses:
        Expense.objects.get_or_create(
            date=ex['date'],
            category=ex['category'],
            amount=ex['amount'],
            description=ex['description']
        )
    
    print(f"Successfully seeded {len(march_expenses)} expenses for April 2026.")

if __name__ == "__main__":
    seed_march_expenses()

import os
import django
from datetime import date, timedelta

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yoga_project.settings')
django.setup()

from core.models import Lesson

def seed_2026_lessons():
    start_date = date(2026, 1, 1)
    end_date = date(2026, 12, 31)
    
    current_date = start_date
    lessons_created = 0
    
    while current_date <= end_date:
        # 0=Monday, 1=Tuesday, ..., 5=Saturday, 6=Sunday
        if current_date.weekday() < 6:
            Lesson.objects.get_or_create(
                date=current_date,
                time='09:00',
                defaults={
                    'max_students': 20,
                    'min_students': 3,
                }
            )
            lessons_created += 1
        current_date += timedelta(days=1)
    
    print(f"Successfully created {lessons_created} lessons for 2026 (Mon-Sat).")

if __name__ == "__main__":
    seed_2026_lessons()

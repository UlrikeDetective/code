import calendar
from datetime import date, datetime, timedelta
from django.shortcuts import render
from .models import Lesson, Customer, Package, Expense

def home(request):
    return render(request, 'home.html')

def lessons(request):
    # Get year and month from query params or default to current
    year = int(request.GET.get('year', date.today().year))
    month = int(request.GET.get('month', date.today().month))
    
    # Calculate previous and next months
    first_day = date(year, month, 1)
    prev_month_date = first_day - timedelta(days=1)
    next_month_date = (first_day + timedelta(days=32)).replace(day=1)
    
    # Get lessons for the current month
    month_lessons = Lesson.objects.filter(
        date__year=year, 
        date__month=month
    ).order_by('date', 'time')
    
    # Create a dictionary of lessons grouped by day for the template
    lessons_by_day = {}
    for lesson in month_lessons:
        day = lesson.date.day
        if day not in lessons_by_day:
            lessons_by_day[day] = []
        lessons_by_day[day].append(lesson)
    
    # Generate the calendar days structure
    cal = calendar.Calendar(firstweekday=0) # Monday is 0
    month_days = cal.monthdays2calendar(year, month)
    
    month_name = calendar.month_name[month]
    
    context = {
        'year': year,
        'month': month,
        'month_name': month_name,
        'prev_year': prev_month_date.year,
        'prev_month': prev_month_date.month,
        'next_year': next_month_date.year,
        'next_month': next_month_date.month,
        'month_days': month_days,
        'lessons_by_day': lessons_by_day,
        'today': date.today(),
    }
    
    return render(request, 'lessons.html', context)

def packages(request):
    return render(request, 'packages.html')

def dashboard(request):
    # Summary data for the owner
    customers_count = Customer.objects.count()
    lessons_count = Lesson.objects.count()
    # Simple profit calculation for demonstration
    total_expenses = sum(e.amount for e in Expense.objects.all())
    # Placeholder for income calculation (will implement package-based logic)
    total_income = 0 
    
    context = {
        'customers_count': customers_count,
        'lessons_count': lessons_count,
        'total_expenses': total_expenses,
        'total_income': total_income,
    }
    return render(request, 'dashboard.html', context)

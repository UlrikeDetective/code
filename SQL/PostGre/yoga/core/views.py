from django.shortcuts import render
from .models import Lesson, Customer, Package, Expense

def home(request):
    return render(request, 'home.html')

def lessons(request):
    upcoming_lessons = Lesson.objects.filter(is_cancelled=False).order_by('date', 'time')
    return render(request, 'lessons.html', {'lessons': upcoming_lessons})

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

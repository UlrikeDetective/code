import calendar
from datetime import date, datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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

def book_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        try:
            customer = Customer.objects.get(email=email)
            if lesson.is_full:
                messages.error(request, "This lesson is already full.")
            elif lesson.is_cancelled:
                messages.error(request, "This lesson is cancelled.")
            elif lesson.attendees.filter(id=customer.id).exists():
                messages.warning(request, "You are already booked for this lesson.")
            else:
                # Check for packages
                package = Package.objects.filter(customer=customer, remaining_lessons__gt=0).order_by('purchase_date').first()
                if package:
                    package.remaining_lessons -= 1
                    package.save()
                    lesson.attendees.add(customer)
                    messages.success(request, f"Successfully booked! You have {package.remaining_lessons} lessons left in your pack.")
                else:
                    messages.error(request, "No active package found. Please buy a package first.")
                    return redirect('packages')
            return redirect('lessons')
        except Customer.DoesNotExist:
            messages.error(request, "Customer with this email not found. Please ask the admin to add you.")
    
    return render(request, 'book_lesson.html', {'lesson': lesson})

def packages(request):
    return render(request, 'packages.html')

def buy_package(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        total_lessons = int(request.POST.get('total_lessons', 1))
        
        # Mapping prices
        prices = {1: 15, 3: 40, 5: 50, 10: 100}
        price_paid = prices.get(total_lessons, 15)

        try:
            customer = Customer.objects.get(email=email)
            Package.objects.create(
                customer=customer,
                total_lessons=total_lessons,
                remaining_lessons=total_lessons,
                price_paid=price_paid
            )
            messages.success(request, f"Successfully purchased {total_lessons} lesson(s) for {price_paid}€.")
            return redirect('lessons')
        except Customer.DoesNotExist:
            messages.error(request, "Customer with this email not found. Please ask the admin to add you.")
            
    return redirect('packages')

def dashboard(request):
    # Summary data for the owner
    customers_count = Customer.objects.count()
    lessons_count = Lesson.objects.count()
    # Profit calculation
    total_expenses = sum(e.amount for e in Expense.objects.all())
    total_income = sum(p.price_paid for p in Package.objects.all())
    
    context = {
        'customers_count': customers_count,
        'lessons_count': lessons_count,
        'total_expenses': total_expenses,
        'total_income': total_income,
    }
    return render(request, 'dashboard.html', context)

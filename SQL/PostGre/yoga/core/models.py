from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Customer(models.Model):
    CUSTOMER_TYPES = [
        ('LOCAL', 'Local Resident'),
        ('VISITOR', 'Visitor'),
    ]
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPES, default='VISITOR')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Package(models.Model):
    PACKAGE_TYPES = [
        (1, 'Single Lesson - 15€'),
        (3, '3 Lessons - 40€'),
        (5, '5 Lessons - 50€'),
        (10, '10 Lessons - 100€'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='packages')
    total_lessons = models.IntegerField(choices=PACKAGE_TYPES)
    remaining_lessons = models.IntegerField()
    purchase_date = models.DateField(default=timezone.now)
    price_paid = models.DecimalField(max_digits=6, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.remaining_lessons = self.total_lessons
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.name} - {self.total_lessons} pack ({self.remaining_lessons} left)"

class Lesson(models.Model):
    date = models.DateField()
    time = models.TimeField(default='09:00')
    max_students = models.IntegerField(default=20)
    min_students = models.IntegerField(default=3)
    attendees = models.ManyToManyField(Customer, related_name='lessons_attended', blank=True)
    is_cancelled = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Lesson on {self.date} at {self.time}"

    @property
    def attendee_count(self):
        return self.attendees.count()

    @property
    def is_full(self):
        return self.attendee_count >= self.max_students

class Expense(models.Model):
    CATEGORIES = [
        ('GAS', 'Gas'),
        ('CAR', 'Car Maintenance'),
        ('ADS', 'Advertising'),
        ('TAX', 'Taxes'),
        ('MAT', 'Yoga Mats'),
        ('OTHER', 'Other'),
    ]
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=10, choices=CATEGORIES)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.get_category_display()} - {self.amount}€ on {self.date}"

class Inventory(models.Model):
    item_name = models.CharField(max_length=100, default='Yoga Mat')
    purchase_date = models.DateField()
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    expected_lifetime_years = models.FloatField(default=1.5)

    def __str__(self):
        return f"{self.quantity}x {self.item_name} purchased on {self.purchase_date}"

    @property
    def replacement_date(self):
        from datetime import timedelta
        return self.purchase_date + timedelta(days=int(self.expected_lifetime_years * 365))

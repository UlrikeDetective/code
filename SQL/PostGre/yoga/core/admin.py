from django.contrib import admin
from .models import Customer, Lesson, Package, Expense, Inventory

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'username', 'city', 'country', 'customer_type', 'created_at')
    list_filter = ('customer_type', 'country', 'city')
    search_fields = ('name', 'email', 'username')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'lesson_type', 'attendee_count', 'is_full', 'is_cancelled')
    list_filter = ('date', 'lesson_type', 'is_cancelled')
    filter_horizontal = ('attendees',)

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('customer', 'package_type', 'total_lessons', 'remaining_lessons', 'purchase_date')
    list_filter = ('purchase_date', 'package_type', 'total_lessons')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'date', 'description')
    list_filter = ('category', 'date')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity', 'purchase_date', 'expected_lifetime_years')

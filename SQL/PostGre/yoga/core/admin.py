from django.contrib import admin
from .models import Customer, Lesson, Package, Expense, Inventory

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'customer_type', 'created_at')
    list_filter = ('customer_type',)
    search_fields = ('name', 'email')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'attendee_count', 'is_full', 'is_cancelled')
    list_filter = ('date', 'is_cancelled')
    filter_horizontal = ('attendees',)

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_lessons', 'remaining_lessons', 'purchase_date')
    list_filter = ('purchase_date', 'total_lessons')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'date', 'description')
    list_filter = ('category', 'date')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity', 'purchase_date', 'expected_lifetime_years')

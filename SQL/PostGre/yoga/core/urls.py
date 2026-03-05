from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lessons/', views.lessons, name='lessons'),
    path('lessons/book/<int:lesson_id>/', views.book_lesson, name='book_lesson'),
    path('packages/', views.packages, name='packages'),
    path('packages/buy/', views.buy_package, name='buy_package'),
    path('packages/check-balance/', views.check_balance, name='check_balance'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

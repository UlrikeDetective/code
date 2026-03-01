from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lessons/', views.lessons, name='lessons'),
    path('packages/', views.packages, name='packages'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from .models import Lesson, Customer, Package
from datetime import date, time, timedelta

class LessonModelTest(TestCase):
    def test_is_in_future(self):
        # Past lesson
        past_date = date.today() - timedelta(days=1)
        past_lesson = Lesson.objects.create(date=past_date, time=time(9, 0))
        self.assertFalse(past_lesson.is_in_future)

        # Future lesson
        future_date = date.today() + timedelta(days=1)
        future_lesson = Lesson.objects.create(date=future_date, time=time(9, 0))
        self.assertTrue(future_lesson.is_in_future)

class BookingViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.customer = Customer.objects.create(
            name="Test User",
            email="test@example.com",
            customer_type='VISITOR'
        )
        self.package = Package.objects.create(
            customer=self.customer,
            total_lessons=5,
            remaining_lessons=5,
            price_paid=50.00
        )

    def test_book_past_lesson_fails(self):
        past_date = date.today() - timedelta(days=1)
        lesson = Lesson.objects.create(date=past_date, time=time(9, 0))
        
        response = self.client.post(reverse('book_lesson', args=[lesson.id]), {
            'email': 'test@example.com'
        })
        
        # Should redirect back to lessons (or stay on same page with error, based on current view logic it redirects to lessons)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(lesson.attendees.count(), 0)
        
        # Follow redirect to check messages
        response = self.client.get(response.url)
        self.assertContains(response, "This lesson has already passed.")

    def test_book_future_lesson_succeeds(self):
        future_date = date.today() + timedelta(days=1)
        lesson = Lesson.objects.create(date=future_date, time=time(9, 0))
        
        response = self.client.post(reverse('book_lesson', args=[lesson.id]), {
            'email': 'test@example.com'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(lesson.attendees.count(), 1)
        
        # Follow redirect to check messages
        response = self.client.get(response.url)
        self.assertContains(response, "Successfully booked!")

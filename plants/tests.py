from django.test import TestCase

from django.contrib.auth.models import User
from .models import Plant, Category, Review


class PlantsTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title='Test Category')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.plant = Plant.objects.create(
            title='Test Plant',
            description='This is a test plant description.',
            category=self.category
        )

    def test_plant_creation(self):
        self.assertEqual(self.plant.title, 'Test Plant')
        self.assertEqual(self.plant.category, self.category)

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_review_creation(self):
        review = Review.objects.create(
            title='Test Review',
            body='This is a test review.',
            user=self.user,
            plant=self.plant,
            estimation=3
        )
        self.assertEqual(review.title, 'Test Review')
        self.assertEqual(review.plant, self.plant)

    # Additional tests for checking image uploads, ratings, and other aspects of Plant, Category, and Review models

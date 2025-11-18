# store/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductModelTest(TestCase):
    def test_str_method(self):
        product = Product.objects.create(name="Laptop", price=999.99, description="High-end", image="image.jpg")
        self.assertEqual(str(product), "Laptop")

class HomePageViewTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'store/home.html')

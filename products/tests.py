from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from .models import Category,Product

class TestProduct(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
                title="Digital",
                slug="digital"
            )

        self.product = Product.objects.create(
                category=self.category,
                title="Mouse Logitexh",
                slug="mouse",
                description=" Mouse",
                image="products/mouse.jpg",
                price=13000000,
                stock=6
            )

    def product_test_list(self):
        url = reverse("shop") 
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200) 
        self.assertEqual(len(response.data), 1)

    def product_test_detail(self):
        url = reverse("product-item", args=["mouse"])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Mouse")

    def product_test_404(self):
        url = reverse("product-item", args=["invalid"])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
        
from django.test import TestCase, Client
# from unittest import TestCase
from shop.models import Product

class TestShopView(TestCase):
    def test_product_view(self):
        client = Client()
        test_product_name = "test_name"
        test_product_price = 100
        Product.objects.create(name=test_product_name, price=test_product_price)
        url = "/shop/add_product"
        response = client.get(path=url)
        success_status_code = 200
        self.assertEqual(response.status_code, success_status_code)



"""
Module returns getting all products results
"""
from unittest import TestCase
from api.tests.create_item import CreateItem

class TestGetProducts(TestCase):
    """
    Class that return the test results for getting all products
    """
    def test_get_all_products(self):
        """
        Method for testing endpoint of getting all products
        """
        CreateItem('products').create_item('Iphone', 3, 10)
        CreateItem('products').create_item('Nokia', 3, 10)
        CreateItem('products').create_item('Sony', 3, 10)

        req = CreateItem('products').client().get('/api/v1/products/')
        self.assertEqual(req.status_code, 200)

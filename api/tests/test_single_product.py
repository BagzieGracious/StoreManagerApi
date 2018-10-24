"""
Module for checking if single product exists
"""
from unittest import TestCase
from api.tests.create_item import CreateItem

class TestSingleProducts(TestCase):
    """
    Class that return the test results for single product
    """
    def test_get_single_product(self):
        """
        Method for testing if product exists
        """
        CreateItem('products').create_item('Iphone', 3, 10)
        CreateItem('products').create_item('Nokia', 3, 10)
        CreateItem('products').create_item('Sony', 3, 10)

        req = CreateItem('products').client().get('/api/v1/products/5')
        self.assertEqual(req.status_code, 200)

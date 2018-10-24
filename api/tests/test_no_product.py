"""
Module for checking if product doesnot exist
"""
from unittest import TestCase
from api.tests.create_item import CreateItem

class TestNoProducts(TestCase):
    """
    Class that return the test results for no product found
    """
    def test_no_product(self):
        """
        Method for testing if product is not found
        """
        CreateItem('products').create_item('Iphone', 3, 10)
        CreateItem('products').create_item('Nokia', 3, 10)
        CreateItem('products').create_item('Sony', 3, 10)

        req = CreateItem('products').client().get('/api/v1/products/10')
        self.assertEqual(req.status_code, 404)

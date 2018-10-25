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
        CreateItem().create_product('Iphone', "best smart phone", 3, 5)
        CreateItem().create_product('Nokia', "best smart phone", 3, 5)
        CreateItem().create_product('Sony', "best smart phone", 3, 5)

        req = CreateItem().client().get('/api/v1/products/10')
        self.assertEqual(req.status_code, 404)

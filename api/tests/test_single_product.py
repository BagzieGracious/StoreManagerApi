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
        CreateItem().create_product('Iphone', "best smart phone", 3, 5)
        CreateItem().create_product('Nokia', "best smart phone", 3, 5)
        CreateItem().create_product('Sony', "best smart phone", 3, 5)

        req = CreateItem().client().get('/api/v1/products/5')
        self.assertEqual(req.status_code, 200)

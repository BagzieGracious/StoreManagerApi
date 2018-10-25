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
        CreateItem().create_product('Iphone', "best smart phone", 3, 5)
        CreateItem().create_product('Nokia', "best smart phone", 3, 5)
        CreateItem().create_product('Sony', "best smart phone", 3, 5)

        req = CreateItem().client().get('/api/v1/products/')
        self.assertEqual(req.status_code, 200)

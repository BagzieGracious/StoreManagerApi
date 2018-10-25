"""
Module for checking if sale doesnot exist
"""
from unittest import TestCase
from api.tests.create_item import CreateItem

class TestNoSale(TestCase):
    """
    Class that return the test results for no sale found
    """
    def test_no_sale(self):
        """
        Method for testing if sale is not found
        """
        CreateItem().create_sale('Iphone', 3, 1045300)
        CreateItem().create_sale('Nokia', 3, 1000900)
        CreateItem().create_sale('Sony', 3, 100000)

        req = CreateItem().client().get('/api/v1/sales/10')
        self.assertEqual(req.status_code, 404)

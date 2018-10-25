"""
Module for checking if single sale exists
"""
from unittest import TestCase
from api.tests.create_item import CreateItem

class TestSingleSale(TestCase):
    """
    Class that return the test results for single sale
    """
    def test_get_single_sale(self):
        """
        Method for testing if sale exists
        """
        CreateItem().create_sale('Iphone', 3, 143500)
        CreateItem().create_sale('Nokia', 3, 100000)
        CreateItem().create_sale('Sony', 3, 1898000)

        req = CreateItem().client().get('/api/v1/sales/5')
        self.assertEqual(req.status_code, 200)

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
        CreateItem('sales').create_item('Iphone', 3, 143500)
        CreateItem('sales').create_item('Nokia', 3, 100000)
        CreateItem('sales').create_item('Sony', 3, 1898000)

        req = CreateItem('products').client().get('/api/v1/sales/5')
        self.assertEqual(req.status_code, 200)

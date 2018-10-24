"""
Module returns getting all sales results
"""
from unittest import TestCase
from api.tests.create_item import CreateItem

class TestGetSales(TestCase):
    """
    Class that return the test results for getting all sales
    """
    def test_get_all_sales(self):
        """
        Method for testing endpoint of getting all sales
        """
        CreateItem('sales').create_item('Iphone', 3, 100000)
        CreateItem('sales').create_item('Nokia', 3, 140000)
        CreateItem('sales').create_item('Sony', 3, 300000)

        req = CreateItem('sales').client().get('/api/v1/sales/')
        self.assertEqual(req.status_code, 200)

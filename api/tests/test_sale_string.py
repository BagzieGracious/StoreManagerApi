"""
Module for checking if sale has string errors
"""
from unittest import TestCase
from flask import json
from api.tests.create_item import CreateItem

class TestSaleStringError(TestCase):
    """
    Class that return the test results for sale with string errors
    """
    def test_sales_with_strings_error(self):
        """
        Method for testing if sale has string errors
        """
        post = CreateItem().create_sale(2, 3, 10)

        resp = json.loads(post.data.decode())
        self.assertFalse(resp['success'], False)
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

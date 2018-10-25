"""
Module for checking if sale has integer errors
"""
from unittest import TestCase
from flask import json
from api.tests.create_item import CreateItem

class TestSaleIntError(TestCase):
    """
    Class that return the test results for sale with integer errors
    """
    def test_product_with_int_error(self):
        """
        Method for testing if quantity and price are integers
        """
        post = CreateItem().create_sale('Iphone', '3', 100000)

        resp = json.loads(post.data.decode())
        self.assertFalse(resp['success'], False)
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

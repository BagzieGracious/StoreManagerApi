"""
Module for checking if product has integer errors
"""
from unittest import TestCase
from flask import json
from api.tests.create_item import CreateItem

class TestProductIntError(TestCase):
    """
    Class that return the test results for product with integer errors
    """
    def test_product_with_int_error(self):
        """
        Method for testing if quantity and min quantity are integers
        """
        post = CreateItem('products').create_item('Iphone', '3', 10)

        resp = json.loads(post.data.decode())
        self.assertFalse(resp['success'], False)
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

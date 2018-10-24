"""
Module for checking if product has string errors
"""
from unittest import TestCase
from flask import json
from api.tests.create_item import CreateItem

class TestProductStringError(TestCase):
    """
    Class that return the test results for product with string errors
    """
    def test_product_with_strings_error(self):
        """
        Method for testing if product has string errors
        """
        post = CreateItem('products').create_item(2, 3, 10)

        resp = json.loads(post.data.decode())
        self.assertFalse(resp['success'], False)
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

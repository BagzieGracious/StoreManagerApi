"""
Module for checking if sale has empty fields
"""
from unittest import TestCase
from flask import json
from api.tests.create_item import CreateItem

class TestSaleEmptyError(TestCase):
    """
    Class that return the test results for sale with empty fields
    """
    def test_sale_with_empty_error(self):
        """
        Method for testing if there is any empty field
        """
        post = CreateItem().create_sale('Iphone', '', 100000)

        resp = json.loads(post.data.decode())
        self.assertFalse(resp['success'], False)
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

"""
Module for checking if product has empty fields
"""
from unittest import TestCase
from flask import json
from api.tests.create_item import CreateItem

class TestProductEmptyError(TestCase):
    """
    Class that return the test results for product with empty feilds
    """
    def test_product_with_empty_error(self):
        """
        Method for testing if there is any empty field
        """
        post = CreateItem().create_product('Iphone', "", 3, 5)

        resp = json.loads(post.data.decode())
        self.assertFalse(resp['success'], False)
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

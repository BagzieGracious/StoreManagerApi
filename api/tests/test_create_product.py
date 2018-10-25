"""
Module for testing create product
"""
from unittest import TestCase
from flask import json
from api.tests.create_item import CreateItem

class TestCreateProduct(TestCase):
    """
    Class that inherits TestCase for testing TDD
    """

    def test_create_product(self):
        """
        Method returns create products results
        """
        post = CreateItem().create_product('Iphone', "best smart phone", 3, 5)

        resp = json.loads(post.data.decode())
        self.assertTrue(resp['success'], True)
        self.assertTrue(resp['payload'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 201)

"""
Module for testing create sale
"""
from unittest import TestCase
from flask import json
from api.tests.create_item import CreateItem

class TestCreateSale(TestCase):
    """
    Class that inherits TestCase for testing TDD
    """

    def test_create_sale(self):
        """
        Method returns create products results
        """
        post = CreateItem('sales').create_item('Iphone', 3, 100000)

        resp = json.loads(post.data.decode())
        self.assertTrue(resp['success'], True)
        self.assertTrue(resp['payload'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 201)

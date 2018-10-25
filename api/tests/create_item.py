from flask import json
from run import APP

class CreateItem:

    def __init__(self):
        self.app = APP
        self.client = self.app.test_client

    def create_product(self, product, description, quantity, min_quantity):
        post = self.client().post(
            '/api/v1/products/',
            data=json.dumps(dict(
                product=product,
                description=description,
                quantity=quantity,
                minQuantity=min_quantity
            )),
            content_type='application/json'
        )
        return post

    def create_sale(self, product, quantity, price):
        post = self.client().post(
            '/api/v1/sales/',
            data=json.dumps(dict(
                product=product,
                quantity=quantity,
                price=price
            )),
            content_type='application/json'
        )
        return post

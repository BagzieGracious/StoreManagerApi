from flask import json
from run import APP

class CreateItem:

    def __init__(self, typ):
        self.typ = typ
        self.app = APP
        self.client = self.app.test_client

    def create_item(self, product, quantity, var=None):
        if self.typ == "sales":
            post = self.client().post(
                '/api/v1/sales/',
                data=json.dumps(dict(
                    product=product,
                    quantity=quantity,
                    price=var
                )),
                content_type='application/json'
            )
            return post

        if self.typ == 'products':
            post = self.client().post(
                '/api/v1/products/',
                data=json.dumps(dict(
                    product=product,
                    quantity=quantity,
                    minQuantity=var
                )),
                content_type='application/json'
            )
            return post
"""
Module for controllers
"""
from flask import request
from api.models.model import Model
from api.data.data import Data
from api.config.data_validation import DataValidation

class Controller:
    """
    Class controller for controlling views
    """
    def __init__(self, typ):
        """
        class contructor that initializes object type
        """
        self.typ = typ
        self.product = Model(Data.all_products())
        self.sale = Model(Data.all_sales())

    def get(self, item_id=None):
        """
        Methods for getting data through endpoints
        """
        if self.typ == 'sales':
            if item_id is None:
                return self.sale.get_item()
            return self.sale.get_item(item_id, 'sale_id')

        if self.typ == 'products':
            if item_id is None:
                return self.product.get_item()
            return self.product.get_item(item_id, 'product_id')


    def post(self):
        """
        Methods for posting or creating an item through endpoints
        """
        data = request.get_json()

        if self.typ == 'sales':
            values = DataValidation().validation(data['product'], data['product'], data['price'])
            if isinstance(values, bool):
                obj = {
                    "sale_id": len(self.sale.get_item()) + 1,
                    "product": data['product'],
                    "quantity": data['quantity'],
                    "price": data['price']
                }
                return self.sale.create_item(obj)
            return values

        if self.typ == 'products':
            values = DataValidation().validation(data['product'], data['product'], data['minQuantity'])
            if isinstance(values, bool):
                obj = {
                    "product_id": len(self.product.get_item()) + 1,
                    "product": data['product'],
                    "quantity": data['quantity'],
                    "minQuantity": data['minQuantity']
                }
                return self.product.create_item(obj)
            return values

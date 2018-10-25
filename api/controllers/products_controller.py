"""
Module to handle products requests via endpoints
"""

from flask import request, jsonify
from flask.views import MethodView
from api.models.model import Model
from api.data.data import Data
from api.config.data_validation import DataValidation

class ProductsController(MethodView):
    """
    Products controller that inherits the method view
    """
    products = Model(Data.all_products())


    @staticmethod
    def get(product_id=None):
        """
        Method that handles view of products
        """
        if product_id is None:
            return ProductsController.products.get_item()
        return ProductsController.products.get_item(product_id, 'product_id')

    @staticmethod
    def post():
        """
        Method that handles create products
        """
        post_data = request.get_json()

        post_values = DataValidation.validate_product(post_data['quantity'], post_data['minQuantity'], post_data['product'], post_data['description'])

        if isinstance(post_values, bool):
            data_object = {
                "product_id": len(ProductsController.products.get_item()) + 1,
                "product": post_data['product'],
                "description": post_data['description'],
                "quantity": post_data['quantity'],
                "minQuantity": post_data['minQuantity']
            }
            return ProductsController.products.create_item(data_object)
        return post_values

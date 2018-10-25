"""
Module to handle products requests via endpoints
"""

from flask import request, jsonify
from flask.views import MethodView
from api.models.product_model import ProductModel
from api.config.data_validation import DataValidation

class ProductsController(MethodView):
    """
    Products controller that inherits the method view
    """
    allProducts = ProductModel.get_products_data()

    @staticmethod
    def get(product_id=None):
        """
        Method that handles view of products
        """
        if product_id is None:
            return jsonify({
                "success":True,
                "payload":ProductModel.get_products_data()
            }), 200
        return ProductModel.get_products_data(product_id)

    @staticmethod
    def post():
        """
        Method that handles create products
        """
        post_data = request.get_json()

        post_values = DataValidation.validate_product(post_data['quantity'], post_data['minQuantity'], post_data['product'], post_data['description'])

        if isinstance(post_values, bool):
            data_object = {
                "product_id": len(ProductsController.allProducts) + 1,
                "product": post_data['product'],
                "description": post_data['description'],
                "quantity": post_data['quantity'],
                "minQuantity": post_data['minQuantity']
            }
            return ProductModel.create_product(data_object)
        return post_values

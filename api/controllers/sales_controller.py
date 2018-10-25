"""
Module to handle sales requests via endpoints
"""

from flask import request, jsonify
from flask.views import MethodView
from api.models.model import Model
from api.data.data import Data
from api.config.data_validation import DataValidation

class SalesController(MethodView):
    """
    Sales controller that inherits the method view
    """
    sales = Model(Data.all_sales())

    @staticmethod
    def get(sale_id=None):
        """
        Method that handles view of sales records
        """
        if sale_id is None:
            return SalesController.sales.get_item()
        return SalesController.sales.get_item(sale_id, 'sale_id')

    @staticmethod
    def post():
        """
        Method that handles create sales
        """
        post_data = request.get_json()
        post_values = DataValidation.validate_sale(post_data['quantity'], post_data['price'], post_data['product'])

        if isinstance(post_values, bool):
            data_object = {
                "sale_id": len(SalesController.sales.get_item()) + 1,
                "product": post_data['product'],
                "quantity": post_data['quantity'],
                "price": post_data['price']
            }
            return SalesController.sales.create_item(data_object)
        return post_values

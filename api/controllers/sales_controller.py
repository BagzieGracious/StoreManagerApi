"""
Module to handle sales requests via endpoints
"""

from flask import request, jsonify
from flask.views import MethodView
from api.models.sales_model import SalesModel
from api.config.data_validation import DataValidation

class SalesController(MethodView):
    """
    Sales controller that inherits the method view
    """
    all_sales = SalesModel.get_all_sales()

    @staticmethod
    def get(sale_id=None):
        """
        Method that handles view of sales records
        """
        if sale_id is None:
            return jsonify(SalesModel.get_all_sales()), 200
        return SalesModel.get_all_sales(sale_id)

    @staticmethod
    def post():
        """
        Method that handles create sales
        """
        post_data = request.get_json()
        post_values = DataValidation.validate_sale(post_data['quantity'], post_data['price'], post_data['product'], post_data['salesAddedDate'])

        if isinstance(post_values, bool):
            data_object = {
                "sale_id": len(SalesController.all_sales) + 1,
                "product": post_data['product'],
                "quantity": post_data['quantity'],
                "price": post_data['price'],
                "salesAddedDate": post_data['salesAddedDate'],
            }
            return SalesModel.create_sales(data_object)
        return post_values

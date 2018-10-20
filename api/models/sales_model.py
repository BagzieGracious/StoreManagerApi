"""
Module to handle sales data stored in data structures
"""

from flask import jsonify
from api.data.data import Data

class SalesModel:
    """
    Sales Model return data to Sales Controller
    """
    sales_list = []

    @staticmethod
    def get_all_sales(sale_id=None):
        """
        Method that gets sales records from data structures
        """
        if sale_id is None:
            return Data.all_sales()

        sale_list = Data.all_sales()
        for sale in sale_list:
            if sale.get('sale_id') == sale_id:
                return jsonify(sale), 200

        return jsonify({"status": "Not Found", "message": "File doesnot exist at this URL"}), 404

    @staticmethod
    def create_sales(new_sale):
        """
        Method for adding sales records in data structures
        """
        SalesModel.sales_list = Data.all_sales()
        new_list = []
        SalesModel.sales_list.append(new_sale)
        new_list = SalesModel.sales_list
        return jsonify({
            "status":"Created",
            "statusMessage":"Your sales were created",
            "statussData":new_list
        }), 201

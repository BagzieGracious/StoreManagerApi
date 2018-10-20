"""
Module to handle products data stored in data structures
"""

from flask import jsonify
from api.data.data import Data

class ProductModel:
    """
    Product Model return data to Products Controller
    """
    prod_list = []

    @staticmethod
    def get_products_data(product_id=None):
        """
        Method that gets data from data structures
        """
        if product_id is None:
            return Data.all_products()

        prod_list = Data.all_products()
        for product in prod_list:
            if product.get('product_id') == product_id:
                return jsonify(product), 200

        return jsonify({"status": "Not Found", "message": "File doesnot exist at this URL"}), 404

    @staticmethod
    def create_product(new_product):
        """
        Method for adding products in data structures
        """
        ProductModel.prod_list = Data.all_products()
        new_list = []
        ProductModel.prod_list.append(new_product)
        new_list = ProductModel.prod_list
        return jsonify({
            "status":"Created",
            "statusMessage":"Your product was created",
            "statussData":new_list
        }), 201

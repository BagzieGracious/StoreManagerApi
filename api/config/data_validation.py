"""
Module to return validations values
"""
from flask import jsonify

class DataValidation:
    """
    Class with methods to return validation values
    """
    @staticmethod
    def product_int_values(quantity, min_quantity):
        """
        Method tests if the params are all integers
        """
        if isinstance(quantity, int) and isinstance(min_quantity, int):
            return True
        return False

    @staticmethod
    def product_str_values(pdt, dsn):
        """
        Method tests if the params are all strings
        """
        if isinstance(pdt, str) and isinstance(dsn, str):
            return True
        return False

    @staticmethod
    def product_empty(qty, min_qty, pdct, dsn):
        """
        Method tests if the params are not empty
        """
        if qty != "" and min_qty != "" and pdct != "" and dsn != "":
            return True
        return False

    @staticmethod
    def validate_product(qty, min_qty, pdct, dsn):
        """"
        Method returns the validation products status
        """
        if DataValidation.product_empty(qty, min_qty, pdct, dsn):
            if DataValidation.product_str_values(pdct, dsn):
                if DataValidation.product_int_values(qty, min_qty):
                    return True
                return jsonify({
                    "success":False,
                    "error": {
                        "code":400,
                        "message":"quanity and minQuantity fields should be integers"
                    }
                }), 400
            return jsonify({
                "success":False,
                "error": {
                    "code":400,
                    "message":"product, and description  fields should be strings"
                }
            }), 400
        return jsonify({
            "success":False,
            "error":{
                "code":400,
                "message":"No field should be empty"
            }
        }), 400

    @staticmethod
    def sales_int_values(quantity, price):
        """
        Method tests if the params are all integers
        """
        if isinstance(quantity, int) and isinstance(price, int):
            return True
        return False

    @staticmethod
    def sales_str_values(product):
        """
        Method tests if the params are all strings
        """
        if isinstance(product, str):
            return True
        return False

    @staticmethod
    def sales_empty(quantity, price, product):
        """
        Method tests if the params are empty
        """
        if quantity != "" and price != "" and product != "":
            return True
        return False

    @staticmethod
    def validate_sale(quantity, price, product):
        """"
        Method returns the validation sales status
        """
        if DataValidation.sales_empty(quantity, price, product):
            if DataValidation.sales_str_values(product):
                if DataValidation.sales_int_values(quantity, price):
                    return True
                return jsonify({
                    "success":False,
                    "error": {
                        "code":400,
                        "message":"quanity and price fields should be integers"
                    }
                }), 400
            return jsonify({
                "success": False,
                "error": {
                    "code":400,
                    "message":"product fields should be a string"
                }
            }), 400
        return jsonify({
            "success":False,
            "error": {
                "code": 400,
                "message":"No field should be empty"
            }
        }), 400

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
    def product_str_values(pdt, dsn, pdt_date):
        """
        Method tests if the params are all strings
        """
        if isinstance(pdt, str) and isinstance(dsn, str) and isinstance(pdt_date, str):
            return True
        return False

    @staticmethod
    def product_empty(qty, min_qty, pdct, dsn, pdt_date):
        """
        Method tests if the params are not empty
        """
        if qty != "" and min_qty != "" and pdct != "" and dsn != "" and pdt_date != "":
            return True
        return False

    @staticmethod
    def validate_product(qty, min_qty, pdct, dsn, pdt_date):
        """"
        Method returns the validation products status
        """
        if DataValidation.product_empty(qty, min_qty, pdct, dsn, pdt_date):
            if DataValidation.product_str_values(pdct, dsn, pdt_date):
                if DataValidation.product_int_values(qty, min_qty):
                    return True
                return jsonify({
                    "status":"Bad Request",
                    "message": "quanity and minQuantity fields should be integers"
                }), 400
            return jsonify({
                "status":"Bad Request",
                "message": "product, description, and productDateAdded fields should be strings"
            }), 400
        return jsonify({"status":"Bad Request", "message": "No field should be empty"}), 400

    @staticmethod
    def sales_int_values(quantity, price):
        """
        Method tests if the params are all integers
        """
        if isinstance(quantity, int) and isinstance(price, int):
            return True
        return False

    @staticmethod
    def sales_str_values(product, sales_date_added):
        """
        Method tests if the params are all strings
        """
        if isinstance(product, str) and isinstance(sales_date_added, str):
            return True
        return False

    @staticmethod
    def sales_empty(quantity, price, product, sales_date_added):
        """
        Method tests if the params are empty
        """
        if quantity != "" and price != "" and product != "" and sales_date_added != "":
            return True
        return False

    @staticmethod
    def validate_sale(quantity, price, product, sales_date_added):
        """"
        Method returns the validation sales status
        """
        if DataValidation.sales_empty(quantity, price, product, sales_date_added):
            if DataValidation.sales_str_values(product, sales_date_added):
                if DataValidation.sales_int_values(quantity, price):
                    return True
                return jsonify({
                    "status":"Bad Request",
                    "message": "quanity and price fields should be integers"
                }), 400
            return jsonify({
                "status":"Bad Request",
                "message": "product, and salesDateAdded fields should be strings"
            }), 400
        return jsonify({"status":"Bad Request", "message": "No field should be empty"}), 400
        
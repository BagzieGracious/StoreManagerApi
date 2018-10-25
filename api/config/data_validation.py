"""
Module to return validations values
"""
from flask import jsonify

class DataValidation:
    """
    Class with methods to return validation values
    """

    def item_int_errors(self, *args):
        """
        Method for checking int errors
        """
        for param in args:
            if not isinstance(param, int):
                return jsonify({
                "success":False,
                "error":{
                    "code":400,
                    "message":"{} should be integers".format(param)
                }
            }), 400
        return True

    def item_string_errors(self, product):
        """
        Methods for checking string error
        """
        if isinstance(product, str):
            return True
        return jsonify({
            "success":False,
            "error":{
                "code":400,
                "message":"product should be a string"
            }
        }), 400

    def item_empty_error(self, *args):
        """
        Methods for checking empty error
        """
        for param in args:
            if param == "":
                return jsonify({
                    "success":False,
                    "error":{
                        "code":400,
                        "message":"empty fields aren't allowed"
                    }
                }), 400
        return True

    def validation(self, quantity, product, var):
        """
        Methods for validity of data
        """
        if isinstance(self.item_empty_error(quantity, product, var), bool):
            if isinstance(self.item_string_errors(product), bool):
                if isinstance(self.item_int_errors(quantity, var), bool):
                    return True
                return self.item_int_errors(quantity, var)
            return self.item_string_errors(product)
        return self.item_empty_error(quantity, product, var)

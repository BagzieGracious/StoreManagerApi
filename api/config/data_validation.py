"""
Module to return validations values
"""
from flask import jsonify

class DataValidation:
    """
    Class with methods to return validation values
    """
    def __init__(self, req, typ):
        self.req = req
        self.typ = typ

    def item_int_errors(self):
        """
        Method for checking int errors
        """
        if self.typ == 'sales':
            if isinstance(self.req['quantity'], int) and isinstance(self.req['price'], int):
                return True
            return jsonify({
                "success":False,
                "error":{
                    "code":400,
                    "message":"quantity and price should be integers"
                }
            }), 400

        if self.typ == 'products':
            if isinstance(self.req['quantity'], int) and isinstance(self.req['minQuantity'], int):
                return True
            return jsonify({
                "success":False,
                "error":{
                    "code":400,
                    "message":"quantity and minQuantity should be integers"
                }
            }), 400

    def item_string_errors(self):
        """
        Methods for checking string error
        """
        if isinstance(self.req['product'], str):
            return True
        return jsonify({
            "success":False,
            "error":{
                "code":400,
                "message":"product should be a string"
            }
        }), 400

    def item_empty_error(self):
        """
        Methods for checking empty error
        """
        if self.typ == 'sales':
            if self.req['product'] != "" and self.req['quantity'] != "" and self.req['price'] != "":
                return True
        if self.typ == 'products':
            if self.req['quantity'] != "" and self.req['minQuantity'] != "" and self.req['product'] != "":
                return True
        return jsonify({
            "success":False,
            "error":{
                "code":400,
                "message":"empty fields aren't allowed"
            }
        }), 400

    def validation(self):
        """
        Methods for validity of data
        """
        if isinstance(self.item_empty_error(), bool):
            if isinstance(self.item_string_errors(), bool):
                if isinstance(self.item_int_errors(), bool):
                    return True
                return self.item_int_errors()
            return self.item_string_errors()
        return self.item_empty_error()

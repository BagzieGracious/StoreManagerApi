"""
Module that acts a model, for handling data manipulation
"""
from flask import jsonify

class Model:
    """
    model class that add data to data structures
    """
    def __init__(self, lst):
        """
        constructor method that initializes a list
        """
        self.lst = lst

    def get_item(self, item_id=None, item_var=None):
        """
        method for get data from data structures
        """
        if item_id is None and item_var is None:
            return jsonify({"success":True, "payload":self.lst}), 200
        for item in self.lst:
            if item.get(item_var) == item_id:
                return jsonify({"success":True, "payload":item}), 200
        return jsonify({"success":False, "error":{"code":404, "message": "not found"}}), 404

    def create_item(self, item):
        """
        method for add an item in the data structure
        """
        return jsonify({"success":True, "payload":item}), 201

"""
Module that returns dummy data
"""

class Data:
    """
    class that returns data stored in data structures
    """
    @staticmethod
    def all_products():
        """
        Method that returns all available products
        """
        return [
            {
                "product_id":1,
                "product":"Iphone",
                "quantity":100,
                "minQuantity":3,
            },
            {
                "product_id":2,
                "product":"HTC",
                "quantity":120,
                "minQuantity":5
            },
            {
                "product_id":3,
                "product":"Samsung",
                "quantity":324,
                "minQuantity":2
            },
            {
                "product_id":4,
                "product":"Nokia",
                "quantity":165,
                "minQuantity":10
            },
            {
                "product_id":5,
                "product":"Motorola",
                "quantity":986,
                "minQuantity":4
            }
        ]

    @staticmethod
    def all_sales():
        """
        Method that returns all record sales
        """
        return [
            {
                "sale_id": 1,
                "product": "Samsung Flatscreen Tv",
                "quantity": 2,
                "price": 4500000
            },
            {
                "sale_id": 2,
                "product": "Toshiba Flatscreen Tv",
                "quantity": 6,
                "price": 9000000
            },
            {
                "sale_id": 3,
                "product": "LG Flatscreen Tv",
                "quantity": 12,
                "price": 1500000
            },
            {
                "sale_id": 4,
                "product": "Sony Flatscreen Tv",
                "quantity": 1,
                "price": 500000
            },
            {
                "sale_id": 5,
                "product": "Hisense Flatscreen Tv",
                "quantity": 2,
                "price": 800000
            },
        ]

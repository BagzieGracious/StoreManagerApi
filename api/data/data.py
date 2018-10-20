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
                "description":"The iPhone is a smartphone developed by Apple foundation",
                "quantity":100,
                "minQuantity":3,
                "productDateAdded":"20:30 03-Jan-2018"
            },
            {
                "product_id":2,
                "product":"HTC",
                "description":"The HTC U12 Life is powered by 1.8GHz",
                "quantity":120,
                "minQuantity":5,
                "productDateAdded":"20:30 03-Feb-2018"
            },
            {
                "product_id":3,
                "product":"Samsung",
                "description":"The Samsung Galaxy S8 is powered by 1.9GHz",
                "quantity":324,
                "minQuantity":2,
                "productDateAdded":"20:30 03-Mar-2018"
            },
            {
                "product_id":4,
                "product":"Nokia",
                "description":"The phone comes with a 6.00-inch",
                "quantity":165,
                "minQuantity":10,
                "productDateAdded":"20:30 03-Apr-2018"
            },
            {
                "product_id":5,
                "product":"Motorola",
                "description":"The phone comes with a 4.50-inch touchscreen",
                "quantity":986,
                "minQuantity":4,
                "productDateAdded":"20:30 03-May-2018"
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
                "price": 4500000,
                "salesAddedDate": "20:30 02-Jan-2018"
            },
            {
                "sale_id": 2,
                "product": "Toshiba Flatscreen Tv",
                "quantity": 6,
                "price": 9000000,
                "salesAddedDate": "20:30 02-Feb-2018"
            },
            {
                "sale_id": 3,
                "product": "LG Flatscreen Tv",
                "quantity": 12,
                "price": 1500000,
                "salesAddedDate": "20:30 02-Mar-2018"
            },
            {
                "sale_id": 4,
                "product": "Sony Flatscreen Tv",
                "quantity": 1,
                "price": 500000,
                "salesAddedDate": "20:30 02-Apr-2018"
            },
            {
                "sale_id": 5,
                "product": "Hisense Flatscreen Tv",
                "quantity": 2,
                "price": 800000,
                "salesAddedDate": "20:30 02-May-2018"
            },
        ]

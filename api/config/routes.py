"""
Module for rendering routes
"""

from api.controllers.products_controller import ProductsController
from api.controllers.sales_controller import SalesController

class Routes:
    """
    Create a Routes class
    """

    @staticmethod
    def fetch_routes(app):
        """
        static method for fetching all routes
        """
        #products endpoints
        app.add_url_rule(
            '/api/v1/products/',
            view_func=ProductsController.as_view('getProducts'),
            methods=['GET'],
            strict_slashes=False
        )
        app.add_url_rule(
            '/api/v1/products/<int:product_id>',
            view_func=ProductsController.as_view('getSingleProduct'),
            methods=['GET'],
            strict_slashes=False
        )
        app.add_url_rule(
            '/api/v1/products/',
            view_func=ProductsController.as_view('createProduct'),
            methods=['POST'],
            strict_slashes=False
        )

        #sales endpoints
        app.add_url_rule(
            '/api/v1/sales/',
            view_func=SalesController.as_view('getSales'),
            methods=['GET'],
            strict_slashes=False
        )
        app.add_url_rule(
            '/api/v1/sales/<int:sale_id>',
            view_func=SalesController.as_view('getSingleSale'),
            methods=['GET'],
            strict_slashes=False
        )
        app.add_url_rule(
            '/api/v1/sales/',
            view_func=SalesController.as_view('createSale'),
            methods=['POST'],
            strict_slashes=False
        )

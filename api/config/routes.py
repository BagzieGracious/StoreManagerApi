"""
Module for rendering routes
"""
from api.controllers.controller import Controller

class Routes:
    """
    Create a Routes class
    """
    prod = Controller('products')
    sales = Controller('sales')

    @staticmethod
    def fetch_routes(app):
        """
        static method for fetching all routes
        """

        #default endpoint
        @app.route('/')
        def index():
            return "<h1>Welcome to store manager</h1> <p>The perfect solution for you.</p>"

        #endpoints for products
        @app.route('/api/v1/products/', methods=['GET'], strict_slashes=False)
        def get_all_products():
            return Routes.prod.get()

        @app.route('/api/v1/products/<int:product_id>', methods=['GET'], strict_slashes=False)
        def get_single_product(product_id):
            return Routes.prod.get(product_id)

        @app.route('/api/v1/products/', methods=['POST'], strict_slashes=False)
        def create_product():
            return Routes.prod.post()

        #endpoints for sales
        @app.route('/api/v1/sales/', methods=['GET'], strict_slashes=False)
        def get_all_sales():
            return Routes.sales.get()

        @app.route('/api/v1/sales/<int:sale_id>', methods=['GET'], strict_slashes=False)
        def get_single_sale(sale_id):
            return Routes.sales.get(sale_id)

        @app.route('/api/v1/sales/', methods=['POST'], strict_slashes=False)
        def create_sales():
            return Routes.sales.post()

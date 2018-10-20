"""
Module returns test results
"""
from unittest import TestCase
from flask import json
from run import APP

class TestStoreManager(TestCase):
    """
    Class for testing system endpoints
    """

    def setUp(self):
        """
        Method for setting up client
        """
        self.app = APP
        self.client = self.app.test_client

    def create_products(self, product, description, quantity, min_quantity, product_date_added):
        """
        Method for adding product
        """
        post_product = self.client().post(
            '/api/v1/products/',
            data=json.dumps(dict(
                product=product,
                description=description,
                quantity=quantity,
                minQuantity=min_quantity,
                productDateAdded=product_date_added
            )),
            content_type='application/json'
        )
        return post_product

    def test_create_product(self):
        """
        Method for testing for create product function
        """
        post = self.create_products('Iphone', 'smartphone', 23, 3, "20:30 15/10/18")
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], 'Created')
        self.assertTrue(post_response['statusMessage'], 'Your product was created')
        self.assertTrue(post_response['statussData'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 201)

    def test_product_with_strings_error(self):
        """
        Method for testing if quantity, min quantity are integers
        """
        post = self.create_products('Iphone', 'smartphone', '23', 3, "20:30 15/01/18")
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], "Bad Request")
        self.assertTrue(post_response['message'], 'product, description, and productDateAdded fields should be strings')
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

    def test_product_with_integers_error(self):
        """
        Method for testing if products, productsAddedDate, and descriptions are strings
        """
        post = self.create_products(1, 'This is the best smartphone', 23, 3, "20:30 15-Jan-2018")
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], "Bad Request")
        self.assertTrue(post_response['message'], 'quanity and minQuantity fields should be integers')
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

    def test_product_with_empty(self):
        """
        Method for testing if one of products fields is empty
        """
        post = self.create_products("", '', 23, 3, "20:30 15-Jan-2018")
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], "Bad Request")
        self.assertTrue(post_response['message'], 'No field should be empty')
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)


    def test_get_all_products(self):
        """
        Method for testing to get all products
        """
        self.create_products('Iphone', 'This is the best smartphone', 23, 3, "20:30 15-Jan-2018")
        self.create_products('Samsung', 'This is the best smartphone', 23, 3, "20:30 15-Feb-2018")
        self.create_products('Techno', 'This is the best smartphone', 23, 3, "20:30 15-Mar-2018")
        self.create_products('LG', 'This is the best smartphone', 23, 3, "20:30 15-Apr-2018")

        request_data = self.client().get('/api/v1/products/')
        self.assertEqual(request_data.status_code, 200)

    def test_get_single_products(self):
        """
        Method for testing to get single products
        """
        self.create_products('Iphone', 'This is the best smartphone', 23, 3, "20:30 15-Jan-2018")
        self.create_products('Samsung', 'This is the best smartphone', 23, 3, "20:30 15-Feb-2018")
        self.create_products('Techno', 'This is the best smartphone', 23, 3, "20:30 15-Mar-2018")
        self.create_products('LG', 'This is the best smartphone', 23, 3, "20:30 15-Apr-2018")

        request_data = self.client().get('/api/v1/products/1/')
        self.assertEqual(request_data.status_code, 200)

    def test_product_doesnt_exist(self):
        """
        Method for testing if a product exists
        """
        self.create_products('Iphone', 'This is the best smartphone', 23, 3, "20:30 15-Jan-2018")
        self.create_products('Samsung', 'This is the best smartphone', 23, 3, "20:30 15-Feb-2018")
        self.create_products('Techno', 'This is the best smartphone', 23, 3, "20:30 15-Mar-2018")
        self.create_products('LG', 'This is the best smartphone', 23, 3, "20:30 15-Apr-2018")

        request_data = self.client().get('/api/v1/products/10/')
        get_response = json.loads(request_data.data.decode())
        self.assertTrue(get_response['status'], "Not Found")
        self.assertTrue(get_response['message'], 'File doesnot exist at this URL')
        self.assertTrue(request_data.content_type, 'application/json')
        self.assertEqual(request_data.status_code, 404)

    def create_sales(self, product, quantity, price, sales_added_date):
        """
        Method that adds sales for testing
        """
        post_product = self.client().post(
            '/api/v1/sales/',
            data=json.dumps(dict(
                product=product,
                quantity=quantity,
                price=price,
                salesAddedDate=sales_added_date
            )),
            content_type='application/json'
        )
        return post_product

    def test_create_sales(self):
        """
        Method for testing if sales can be added
        """
        post = self.create_sales('Iphone', 3, 3000000, "20:30 15-Jan-2018")
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], 'Created')
        self.assertTrue(post_response['statusMessage'], 'Your product was created')
        self.assertTrue(post_response['statussData'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 201)

    def test_sales_with_strings_error(self):
        """
        Method for testing if product and sales date added are strings
        """
        post = self.create_sales(34, 3, 3000000, "20:30 15-Jan-2018")
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], "Bad Request")
        self.assertTrue(post_response['message'], 'product, and salesDateAdded fields should be strings')
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

    def test_sales_with_integers_error(self):
        """
        Method for testing price and quantity are integers
        """
        post = self.create_sales("Iphone", "3", 3000000, "20:30 15-Jan-2018")
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], "Bad Request")
        self.assertTrue(post_response['message'], 'quanity and price fields should be integers')
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

    def test_sales_with_empty(self):
        """
        Method for testing if one of sales fields is empty
        """
        post = self.create_sales("Iphone", "", 3000000, "20:30 15-Jan-2018")
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], "Bad Request")
        self.assertTrue(post_response['message'], 'No field should be empty')
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

    def test_get_all_sales(self):
        """
        Method for testing all sales records
        """
        self.create_sales("Iphone", 3, 3000000, "20:30 15-Jan-2018")
        self.create_sales("Tecno", 78, 6000000, "20:30 15-Feb-2018")
        self.create_sales("Itel", 98, 5000000, "20:30 15-Mar-2018")

        request_data = self.client().get('/api/v1/sales/')
        self.assertEqual(request_data.status_code, 200)

    def test_get_single_sales(self):
        """
        Method for testing single sales record
        """
        self.create_sales("Iphone", 3, 3000000, "20:30 15-Jan-2018")
        self.create_sales("Tecno", 78, 6000000, "20:30 15-Feb-2018")
        self.create_sales("Itel", 98, 5000000, "20:30 15-Mar-2018")

        request_data = self.client().get('/api/v1/sales/1/')
        self.assertEqual(request_data.status_code, 200)

    def test_sales_doesnt_exist(self):
        """
        Method for testing if sales record doestnot exist
        """
        self.create_sales("Iphone", 3, 3000000, "20:30 15-Jan-2018")
        self.create_sales("Tecno", 78, 6000000, "20:30 15-Feb-2018")
        self.create_sales("Itel", 98, 5000000, "20:30 15-Mar-2018")

        request_data = self.client().get('/api/v1/sales/10/')
        get_response = json.loads(request_data.data.decode())
        self.assertTrue(get_response['status'], "Not Found")
        self.assertTrue(get_response['message'], 'File doesnot exist at this URL')
        self.assertTrue(request_data.content_type, 'application/json')
        self.assertEqual(request_data.status_code, 404)

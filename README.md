# StoreManagerApi

[![Build Status](https://travis-ci.com/BagzieGracious/StoreManagerApi.svg?branch=feature)](https://travis-ci.com/BagzieGracious/StoreManagerApi)                                                                                 [![Maintainability](https://api.codeclimate.com/v1/badges/54c0c8b76094d0d34563/maintainability)](https://codeclimate.com/github/BagzieGracious/StoreManagerApi/maintainability) 
 [![Codacy Badge](https://api.codacy.com/project/badge/Grade/3cd1cf89c2e54b999fceee410fd64452)](https://www.codacy.com/app/BagzieGracious/StoreManagerApi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BagzieGracious/StoreManagerApi&amp;utm_campaign=Badge_Grade)             [![Coverage Status](https://coveralls.io/repos/github/BagzieGracious/StoreManagerApi/badge.svg?branch=feature)](https://coveralls.io/github/BagzieGracious/StoreManagerApi?branch=feature)                                                              
# StoreManagerApi
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.

**Application Features**

* Store attendant can search and add products to buyer’s cart.
* Store attendant can see his/her sale records but can’t modify them.
* App should show available products, quantity and price.
* Store owner can see sales and can filter by attendants.
* Store owner can add, modify and delete products.


# A user can perform the following :
 As a store attendant:
 - Store attendant can search and add products to buyer’s cart.
 - Store attendant can see his/her sale records but can’t modify them.
 
 As Store Owner:
- Store owner can see sales and can filter by attendants
- Store owner can add, modify and delete products

 Use the following endpoints to perform the specified tasks 
    
    EndPoint                                           | Functionality
    ------------------------                           | ----------------------
    Get /products/                                     | Fetch all products
    Get /products/<product_id>                         | Fetch specific product
    POST /products/                                    | Create a product
    GET /sales/                                        | Retrieves all sales records
    GET /sales/<sales_id>                              | Retrieve a specific sales record
    POST /sales/                                       | Create a sales record
    
**Getting started with the app**

**Technologies used to build the application**

* [Python 3.6.1](https://docs.python.org/3/)

* [Flask](http://flask.pocoo.org/)

# Installation

Create a new directory and initialize git in it. Clone this repository by running
```sh
$ git clone https://github.com/BagzieGracious/Store-Manager-Api-.git
```
Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using
```sh
$ virtualenv venv
```
Activate the virtual environment
```sh
$ cd venv/scripts/activate.bat
```
Install the dependencies in the requirements.txt file using pip
```sh
$ pip install -r requirements.txt
```

Start the application by running
```sh
$ python run.py
```
Test your setup using a client app like postman

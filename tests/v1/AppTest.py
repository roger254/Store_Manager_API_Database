import sys

import json
import os
import unittest

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from app import create_app
from .test_db import migrate, drop, create_admin_user


class AppBaseTest(unittest.TestCase):
    """Base class for all test"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            drop()
            migrate()
            create_admin_user()

        self.default_admin = {
            'username': 'root254',
            'password': 'root1234'
        }
        self.test_user = {
            'username': 'roger254',
            'password': 'test1234'
        }
        self.test_user_incorrect_password = {
            'username': 'roger254',
            'password': 'Test1234'
        }
        self.unavailable_username = {
            'password': 'test1234'
        }
        self.unavailable_password = {
            'username': 'roger254'
        }
        self.int_username = {
            'username': '123456',
            'password': 'test1234'
        }
        self.invalid_username = {
            'username': '!-***%45667',
            'password': 'test1234'
        }
        self.invalid_password = {
            'username': 'roger254',
            'password': 'erg'
        }

        # Product test case
        self.test_product = {
            'p_name': 'Product 1',
            'p_price': 45.5,
            'p_quantity': 50
        }
        self.test_product_2 = {
            'p_name': "Product 2",
            'p_price': 50.5,
            'p_quantity': 12
        }
        self.missing_product_name = {
            'p_price': 45.5,
            'p_quantity': 50
        }
        self.missing_product_price = {
            'p_name': "Product 1",
            'p_quantity': 50
        }
        self.missing_product_quantity = {
            'p_name': 'Product 1',
            'p_price': 45.5
        }
        self.invalid_product_name = {
            'p_name': '123456',
            'p_price': 45.5,
            'p_quantity': 50
        }
        self.invalid_product_price = {
            'p_name': 'Product 1',
            'p_price': 'price',
            'p_quantity': 50
        }
        self.invalid_product_quantity = {
            'p_name': 'Product 1',
            'p_price': 45.5,
            'p_quantity': 'fifty'
        }
        self.test_sale = {
            's_name': 'Product 1',
            's_quantity': 10
        }
        self.missing_sale_name = {
            's_quantity': 10
        }
        self.missing_sale_quantity = {
            's_name': 'Product 1'
        }
        self.invalid_sale_name = {
            's_name': '123456',
            's_quantity': 10
        }
        self.invalid_sale_quantity = {
            's_name': 'Product 1',
            's_quantity': 'Rog34'
        }
        self.unavailable_product_sale = {
            's_name': 'Product 17',
            's_quantity': 10
        }
        self.sale_exceeding_product_quantity = {
            's_name': 'Product 1',
            's_quantity': 456
        }

    def register_test_user(self, data, access_token=None):
        """Register a test user"""
        if access_token is None:
            access_token = self.get_admin_access_token()
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        res = self.client.post(
            'api/v1/register/',
            data=data,
            headers=headers
        )
        return res

    def login_test_user(self):
        """Login registered test user"""

        self.register_test_user(self.test_user)
        res = self.client.post(
            'api/v1/login/',
            data=self.test_user
        )
        return res

    def login_test_admin(self):
        """login registered admin"""
        res = self.client.post(
            'api/v1/login/',
            data=self.default_admin
        )
        return res

    def get_admin_access_token(self):
        """Return admins access token"""
        res = self.login_test_admin()
        return res.json['access_token']

    def get_user_access_token(self):
        """Return login user access token"""
        res = self.login_test_user()
        return res.json['access_token']

    def post_product(self, data, access_token=None):
        """Post product provided data"""
        if access_token is None:
            access_token = self.get_admin_access_token()
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            "content-type": "application/json"
        }
        res = self.client.post(
            'api/v1/product/',
            data=json.dumps(data),
            headers=headers
        )
        return res

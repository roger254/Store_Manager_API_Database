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

        self.test_user = {
            'username': 'roger254',
            'password': 'test1234'
        }
        self.admin_data = {
            'username': 'root254',
            'password': 'root1234'
        }
        self.missing_user_name = {
            'password': 'test134'
        }
        self.missing_user_password = {
            'username': 'Test User 1'
        }
        self.invalid_user_data = {
            'username': 'r45',
            'password': 'rr'
        }
        self.test_user_invalid_pass = {
            'username': 'roger254',
            'password': 'test123454'
        }
        self.create_product = {
            'p_name': 'Product 1',
            'p_price': 55.7,
            'p_quantity': 23
        }
        self.update_product = {
            'p_name': 'Product 2',
            'p_price': 45.6,
            'p_quantity': 45
        }
        self.missing_p_name = {
            'p_price': 34.5,
            'p_quantity': 34
        }
        self.missing_p_price = {
            'p_name': 'Product 2',
            'p_quantity': 34
        }
        self.missing_p_quantity = {
            'p_name': ' Product 3',
            'p_price': 34.5
        }
        self.invalid_product_data = {
            'p_name': "***bb$%6",
            'p_price': "34mmin",
            'p_quantity': "re345"
        }
        self.create_sale = {
            's_name': "Product 1",
            's_quantity': 10
        }
        self.missing_sale_name = {
            's_price': 10
        }
        self.missing_sale_price = {
            's_name': 'Product 1'
        }
        self.unavailable_product_sale = {
            's_name': 'Product 6',
            's_price': 12
        }
        self.exceeding_quantity = {
            's_name': 'Product 1',
            's_quantity': 50
        }

    def post_product(self):
        """post new product"""
        access_token = self.get_admin_token()
        # create item
        response = self.client.post(
            'api/v1/product/',
            data=json.dumps(self.create_product),
            headers=dict(
                Authorization="Bearer " + access_token
            )
        )
        return response

    def post_sale(self):
        """Post new Sale"""
        access_token = self.get_user_token()
        res = self.client.post(
            'api/v1/sales/',
            data=json.dumps(self.create_sale),
        )
        return res

    def register(self):
        """Create new user"""
        response = self.client.post(
            'api/v1/register/',
            data=json.dumps(self.test_user)
        )
        return response

    def login(self):
        """Login created User"""
        res = self.client.post(
            'api/v1/login/',
            data=json.dumps(self.test_user),
        )
        return res

    def admin_login(self):
        """Login created User"""
        res = self.client.post(
            'api/v1/login/',
            data=json.dumps(self.admin_data),
            headers={'content-type': 'application/json'}
        )
        return res

    def get_user_token(self):
        """Get user Token"""
        self.register()
        res = self.login()
        access_token = json.loads(res.data).get('access_token')

        return access_token

    def get_admin_token(self):
        """Get user Token"""
        res = self.admin_login()
        print(res.data)
        access_token = json.loads(res.data).get('access_token')
        print(access_token)
        return access_token

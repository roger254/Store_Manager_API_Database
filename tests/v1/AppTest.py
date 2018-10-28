import sys

import os
import unittest

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from app import create_app
from .test_db import migrate, drop


class AppBaseTest(unittest.TestCase):
    """Base class for all test"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            drop()
            migrate()
            # create_admin_user()

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
        self.missing_product_name = {
            'p_price': 45.5,
            'p_quantity': 50
        }
        self.missing_product_price = {
            'p_name': "Product 1",
            'p_quantity': 50
        }

    def register_test_user(self):
        """Register a test user"""
        res = self.client.post(
            'api/v1/register/',
            data=self.test_user
        )
        return res

    def login_test_user(self):
        """Login registered test user"""
        self.register_test_user()
        res = self.client.post(
            'api/v1/login/',
            data=self.test_user
        )
        return res

import sys

import json
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from tests.v1.AppTest import AppBaseTest


class UserTestCase(AppBaseTest):
    """User Test Case"""

    def test_register(self):
        """Test user Registration"""
        res = self.register()
        self.assertEqual(res.status_code, 201)

    def test_login(self):
        """Test user login"""
        self.register()
        res = self.login()
        self.assertEqual(res.status_code, 200)

    def test_admin_login(self):
        """Test admin login"""
        res = self.admin_login()
        self.assertEqual(res.status_code, 200)

    def test_invalid_password(self):
        """Test for incorrect pass"""
        self.register()
        res = self.client.post(
            'api/v1/auth/login',
            data=json.dumps(self.test_invalid_password()),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(res.status_code, 401)

    def test_missing_username_registration(self):
        """Test registration without username"""
        response = self.client.post(
            'api/v1/auth/register',
            data=json.dumps(self.missing_user_name),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 401)

    def test_missing_password_registration(self):
        """Test registration without password"""
        response = self.client.post(
            'api/v1/auth/register',
            data=json.dumps(self.missing_user_password),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 401)

    def test_user_invalid_data(self):
        """Test user registration with invalid data"""
        response = self.client.post(
            'api/v1/auth/register',
            data=json.dumps(self.invalid_user_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 401)

import sys

import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from tests.v1.AppTest import AppBaseTest


class UserTestCase(AppBaseTest):
    """User Test Case"""

    def test_user_registration(self):
        """Test user registration"""

        res = self.register_test_user(self.test_user)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(self.test_user['username'], res.json['user']['username'])

    def test_missing_username(self):
        """Test user with missing username"""
        res = self.register_test_user(self.unavailable_username)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Username must be provided', res.json['message'])

    def test_missing_password(self):
        """Test registration without password"""

        res = self.register_test_user(self.unavailable_password)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Password must be provided', res.json['message'])

    def test_string_username(self):
        """Test User must be a string"""

        res = self.register_test_user(self.int_username)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Username must be a string', res.json['message'])

    def test_invalid_username(self):
        """Test user registration with invalid username"""
        res = self.register_test_user(self.invalid_username)
        self.assertEqual(res.status_code, 400)
        self.assertEqual('Please enter a valid name', res.json['message']['message'])

    def test_invalid_password(self):
        """Test user registration with invalid password"""
        res = self.register_test_user(self.invalid_password)
        self.assertEqual(res.status_code, 400)
        self.assertEqual('Please enter a valid password', res.json['message']['message'])

    def test_user_cannot_register_twice(self):
        """Test user cannot register twice"""
        access_token = self.get_admin_access_token()
        res = self.register_test_user(self.test_user, access_token=access_token)
        self.assertEqual(res.status_code, 201)

        res = self.register_test_user(data=self.test_user, access_token=access_token)
        self.assertEqual(res.status_code, 400)
        self.assertIn(
            'User {} already exists'.format(self.test_user['username']),
            res.json['message']
        )

    def test_missing_username_login(self):
        """Test login without username"""
        res = self.client.post(
            'api/v1/login/',
            data=self.unavailable_username
        )
        self.assertEqual(res.status_code, 400)
        self.assertEqual('Username is required', res.json['message'])

    def test_missing_password_login(self):
        """Test user login without password"""
        res = self.client.post(
            'api/v1/login/',
            data=self.unavailable_password
        )
        self.assertEqual(res.status_code, 400)
        self.assertIn('Password is required', res.json['message'])

    def test_invalid_login_username(self):
        """Test if user logs in with invalid username"""
        res = self.client.post(
            'api/v1/login/',
            data=self.invalid_username
        )
        self.assertEqual(res.status_code, 400)
        self.assertEqual("Please enter a valid name", res.json['message']['message'])

    def test_invalid_login_password(self):
        """Test invalid login password"""
        res = self.client.post(
            'api/v1/login/',
            data=self.invalid_password
        )
        self.assertEqual(res.status_code, 400)
        self.assertIn('Please enter a valid password', res.json['message']['message'])

    def test_string_username_login(self):
        """Test login with a non string username"""
        res = self.client.post(
            'api/v1/login/',
            data=self.int_username
        )
        self.assertEqual(res.status_code, 400)
        self.assertIn('Username must be a string', res.json['message'])

    def test_unregistered_user(self):
        """Test login with an unregistered user"""
        res = self.client.post(
            'api/v1/login/',
            data=self.test_user
        )
        self.assertEqual(res.status_code, 404)
        self.assertIn('User not found', res.json['message'])

    def test_incorrect_login_password(self):
        """Test if user uses an incorrect password"""
        res = self.register_test_user(self.test_user)
        self.assertEqual(res.status_code, 201)

        res = self.client.post(
            'api/v1/login/',
            data=self.test_user_incorrect_password
        )
        self.assertEqual(res.status_code, 400)
        self.assertIn('Password is incorrect', res.json['message'])

    def test_successful_login(self):
        """Test user successfully logs in"""
        res = self.register_test_user(self.test_user)
        self.assertEqual(res.status_code, 201)
        res = self.client.post(
            'api/v1/login/',
            data=self.test_user
        )
        self.assertEqual(res.status_code, 200)
        self.assertIn('Successfully logged in', res.json['message'])
        self.assertIn('access_token', res.json)

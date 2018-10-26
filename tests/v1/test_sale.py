import sys

import json
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from tests.v1.AppTest import AppBaseTest


class SaleTestCase(AppBaseTest):
    """Sale Test Case"""

    def test_get_access_token(self):
        """Test the access token"""
        res = self.login()
        self.assertEqual(res.status_code, 200)
        self.assertIn('access_token', json.loads(res.data))

    def test_sale_creation(self):
        """Test creating sale"""
        self.get_user_token()
        self.post_product()
        res = self.post_sale()
        self.assertEqual(res.status_code, 201)

    def test_admin_making_sale(self):
        """Testing if admin can make sale post"""
        self.get_admin_token()
        self.post_product()
        res = self.post_sale()
        self.assertEqual(res.status_code, 400)

    def test_unavailable_product_sale(self):
        """Test sale for an unavailable product"""
        access_token = self.get_user_token()
        self.post_product()
        bearer = 'Bearer {}'.format(access_token)
        res = self.client.post(
            'api/v1/sales/',
            data=json.dumps(self.unavailable_product_sale),
        )
        self.assertEqual(res.status_code, 400)

    def test_missing_sale_name(self):
        """Test post sale without name"""
        access_token = self.get_user_token()
        self.post_product()
        res = self.client.post(
            'api/v1/sales/',
            data=json.dumps(self.missing_sale_name),
        )
        self.assertEqual(res.status_code, 400)

    def test_missing_sale_price(self):
        """Test post sale without price"""
        access_token = self.get_user_token()
        self.post_product()
        res = self.client.post(
            'api/v1/sales/',
            data=json.dumps(self.missing_sale_price),
        )
        self.assertEqual(res.status_code, 400)

    def test_sale_exceeding_product_quantity(self):
        """Test sale with exceeding quantity than product"""
        access_token = self.get_user_token()
        self.post_product()
        res = self.client.post(
            'api/v1/sales/',
            data=json.dumps(self.exceeding_quantity),
        )
        self.assertEqual(res.status_code, 400)

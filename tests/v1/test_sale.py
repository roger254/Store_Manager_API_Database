import sys

import json
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from tests.v1.AppTest import AppBaseTest


class SaleTestCase(AppBaseTest):
    """Sale Test Case"""

    # def test_get_access_token(self):
    #     """Test the access token"""
    #     res = self.login()
    #     self.assertEqual(res.status_code, 200)
    #     self.assertIn('access_token', json.loads(res.data))
    #
    # def test_sale_creation(self):
    #     """Test creating sale"""
    #     access_token = self.get_user_token()
    #     self.post_product(access_token)
    #     res = self.post_sale(access_token)
    #     self.assertEqual(res.status_code, 201)
    #
    # def test_admin_making_sale(self):
    #     """Testing if admin can make sale post"""
    #
    #     access_token = self.get_admin_token()
    #     self.post_product(access_token)
    #     headers = {
    #         'Authorization': 'Bearer {}'.format(access_token),
    #         "content-type": "application/json"
    #     }
    #     res = self.client.post(
    #         'api/v1/sales/',
    #         data=json.dumps(self.create_sale),
    #         headers=headers
    #     )
    #     self.assertEqual(res.status_code, 400)
    #
    # def test_unavailable_product_sale(self):
    #     """Test sale for an unavailable product"""
    #     access_token = self.get_user_token()
    #     self.post_product(access_token)
    #     headers = {
    #         'Authorization': 'Bearer {}'.format(access_token),
    #         "content-type": "application/json"
    #     }
    #     res = self.client.post(
    #         'api/v1/sales/',
    #         data=json.dumps(self.unavailable_product_sale),
    #         headers=headers
    #     )
    #     self.assertEqual(res.status_code, 404)
    #
    # def test_missing_sale_name(self):
    #     """Test post sale without name"""
    #     access_token = self.get_user_token()
    #     self.post_product(access_token)
    #     headers = {
    #         'Authorization': 'Bearer {}'.format(access_token),
    #         "content-type": "application/json"
    #     }
    #     res = self.client.post(
    #         'api/v1/sales/',
    #         data=json.dumps(self.missing_sale_name),
    #         headers=headers
    #     )
    #     self.assertEqual(res.status_code, 400)
    #
    # def test_missing_sale_price(self):
    #     """Test post sale without price"""
    #     access_token = self.get_user_token()
    #     self.post_product(access_token)
    #     headers = {
    #         'Authorization': 'Bearer {}'.format(access_token),
    #         "content-type": "application/json"
    #     }
    #     res = self.client.post(
    #         'api/v1/sales/',
    #         data=json.dumps(self.missing_sale_price),
    #         headers=headers
    #     )
    #     self.assertEqual(res.status_code, 400)
    #
    # def test_sale_exceeding_product_quantity(self):
    #     """Test sale with exceeding quantity than product"""
    #     access_token = self.get_user_token()
    #     self.post_product(access_token)
    #     headers = {
    #         'Authorization': 'Bearer {}'.format(access_token),
    #         "content-type": "application/json"
    #     }
    #     res = self.client.post(
    #         'api/v1/sales/',
    #         data=json.dumps(self.exceeding_quantity),
    #         headers=headers
    #     )
    #     self.assertEqual(res.status_code, 400)

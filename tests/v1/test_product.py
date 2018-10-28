import sys

import json
import os
import unittest

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from tests.v1.AppTest import AppBaseTest


class ProductTestCase(AppBaseTest):
    """Product Test Case"""

#     def test_get_access_token(self):
#         """Test access_token"""
#         res = self.admin_login()
#
#         self.assertEqual(res.status_code, 200)
#         self.assertIn('access_token', json.loads(res.data))
#
#     def test_product_creation(self):
#         """Test creating new product"""
#         access_token = self.get_admin_token()
#         res = self.post_product(access_token)
#         self.assertEqual(res.status_code, 201)
#
#     def test_invalid_product(self):
#         """TEst invalid product input"""
#         access_token = self.get_admin_token()
#
#         headers = {
#             'Authorization': 'Bearer {}'.format(access_token),
#             "content-type": "application/json"
#         }
#         response = self.client.post(
#             'api/v1/product/',
#             data=json.dumps(self.invalid_product_data),
#             headers=headers
#         )
#         self.assertEqual(response.status_code, 400)
#
#     def test_missing_product_name(self):
#         """Test missing product name"""
#         access_token = self.get_admin_token()
#         headers = {
#             'Authorization': 'Bearer {}'.format(access_token),
#             "content-type": "application/json"
#         }
#         response = self.client.post(
#             'api/v1/product/',
#             data=json.dumps(self.missing_p_name),
#             headers=headers
#         )
#         self.assertEqual(response.status_code, 400)
#
#     def test_missing_product_price(self):
#         """Test missing product price"""
#
#         access_token = self.get_admin_token()
#         headers = {
#             'Authorization': 'Bearer {}'.format(access_token),
#             "content-type": "application/json"
#         }
#         response = self.client.post(
#             'api/v1/product/',
#             data=json.dumps(self.missing_p_price),
#             headers=headers
#         )
#         self.assertEqual(response.status_code, 400)
#
#     def test_missing_product_quantity(self):
#         """Test missing product quantity"""
#
#         access_token = self.get_admin_token()
#         headers = {
#             'Authorization': 'Bearer {}'.format(access_token),
#             "content-type": "application/json"
#         }
#         response = self.client.post(
#             'api/v1/product/',
#             data=json.dumps(self.missing_p_quantity),
#             headers=headers
#         )
#         self.assertEqual(response.status_code, 400)
#
#     def test_update_product(self):
#         """Test Update product"""
#         access_token = self.get_admin_token()
#         self.post_product(access_token)
#         headers = {
#             'Authorization': 'Bearer {}'.format(access_token),
#             "content-type": "application/json"
#         }
#         res = self.client.put(
#             'api/v1/product/1',
#             data=json.dumps(self.update_product),
#             headers=headers
#         )
#         self.assertEqual(res.status_code, 200)
#
#     def test_update_not_existing_product(self):
#         """Test update of an non existing product"""
#         access_token = self.get_admin_token()
#         headers = {
#             'Authorization': 'Bearer {}'.format(access_token),
#             "content-type": "application/json"
#         }
#         res = self.client.put(
#             'api/v1/product/1',
#             data=json.dumps(self.update_product),
#             headers=headers
#         )
#         self.assertEqual(res.status_code, 401)
#
#     def test_get_all_products(self):
#         """Test all product"""
#         access_token = self.get_admin_token()
#         self.post_product(access_token)
#         headers = {
#             'Authorization': 'Bearer {}'.format(access_token),
#             "content-type": "application/json"
#         }
#         res = self.client.post(
#             'api/v1/product/',
#             headers=headers
#         )
#         self.assertEqual(res.status_code, 200)
#
#     def test_get_specific_product(self):
#         """Test can get specific product"""
#         access_token = self.get_admin_token()
#         self.post_product(access_token)
#         res = self.client.get(
#             'api/v1/product/1',
#             headers={"content-type": "application/json"},
#         )
#         self.assertEqual(res.status_code, 200)
#
#     def test_delete_existing_product(self):
#         """Test deleting existing prod"""
#         access_token = self.get_admin_token()
#         self.post_product(access_token)
#         headers = {
#             'Authorization': 'Bearer {}'.format(access_token),
#             "content-type": "application/json"
#         }
#         res = self.client.delete(
#             'api/v1/product/1',
#             headers=headers
#         )
#         self.assertEqual(res.status_code, 200)
#
#     def test_delete_non_existing_product(self):
#         """Test deleting an non existing product"""
#         access_token = self.get_admin_token()
#         headers = {
#             'Authorization': 'Bearer {}'.format(access_token),
#             "content-type": "application/json"
#         }
#         res = self.client.delete(
#             'api/v1/product/1',
#             headers=headers
#         )
#         self.assertEqual(res.status_code, 404)
#
#
# if __name__ == '__main__':
#     unittest.main()

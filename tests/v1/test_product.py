import sys

import json
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from tests.v1.AppTest import AppBaseTest


class ProductTestCase(AppBaseTest):
    """Product Test Case"""

    def post_product(self, data, access_token=None):
        """Post product provided data"""
        if access_token is None:
            access_token = self.get_user_access_token()
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

    def test_can_post_a_product(self):
        """Test admin can post a product"""

        access_token = self.get_user_access_token()
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            "content-type": "application/json"
        }
        res = self.client.post(
            'api/v1/product/',
            data=json.dumps(self.test_product),
            headers=headers
        )
        self.assertEqual(res.status_code, 201)

    def test_missing_product_name(self):
        """Test creating product without product name"""
        res = self.post_product(self.missing_product_name)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Product name is required', res.json['message'])

    def test_missing_product_price(self):
        """Test creation of a product without price"""
        res = self.post_product(self.missing_product_price)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Product price is required', res.json['message'])

    def test_missing_product_quantity(self):
        """Test creation of a product without quantity"""
        res = self.post_product(self.missing_product_quantity)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Product quantity is required', res.json['message'])

    def test_invalid_product_name(self):
        """Test creation of a product with an invalid name"""
        res = self.post_product(self.invalid_product_name)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Please enter a valid product name', res.json['message'])

    def test_invalid_product_price(self):
        """Test creation of a product with an invalid price"""
        res = self.post_product(self.invalid_product_price)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Product price must be a float', res.json['message'])

    def test_invalid_product_quantity(self):
        """Test creation of a product with an invalid quantity"""
        res = self.post_product(self.invalid_product_quantity)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Product quantity must be an int', res.json['message'])

    def test_creation_of_duplicate_product(self):
        """Test creation of a product twice"""
        res = self.post_product(self.test_product)
        self.assertEqual(res.status_code, 201)
        res = self.post_product(self.test_product)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Product already exists', res.json['message'])

    def test_can_get_all_products(self):
        """Test user can fetch all products"""
        access_token = self.get_user_access_token()

        res = self.post_product(self.test_product, access_token=access_token)
        res2 = self.post_product(self.test_product_2, access_token=access_token)
        self.assertEqual(res.status_code and res2.status_code, 201)
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
        }
        res3 = self.client.get(
            'api/v1/product/',
            headers=headers
        )
        self.assertEqual(res3.status_code, 200)

    def test_user_can_get_specific_item(self):
        """Test user can get a specific item"""
        access_token = self.get_user_access_token()
        res = self.post_product(self.test_product, access_token=access_token)
        self.assertEqual(res.status_code, 201)
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
        }
        res2 = self.client.get(
            'api/v1/product/1',
            headers=headers
        )
        self.assertEqual(res2.status_code, 201)
        self.assertIn(self.test_product['p_name'], res2.json['Product']['p_name'])

    def test_can_update_a_product(self):
        """Test admin can update a product"""
        access_token = self.get_user_access_token()
        res = self.post_product(self.test_product, access_token=access_token)
        self.assertEqual(res.status_code, 201)

        self.test_product['p_quantity'] = 45
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
        }
        res = self.client.put(
            'api/v1/product/',
            data=self.test_product,
            headers=headers,
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(self.test_product['p_quantity'], int(res.json['product']['p_quantity']))

    def test_updating_non_existing_product(self):
        """Test updating a unavailable product"""
        access_token = self.get_user_access_token()
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        res = self.client.put(
            'api/v1/product/',
            data=self.test_product,
            headers=headers
        )
        self.assertEqual(res.status_code, 400)
        self.assertIn(
            'Product {} not found'.format(self.test_product['p_name']),
            res.json['message']
        )

    def test_can_delete_product(self):
        """Test admin can delete product"""
        access_token = self.get_user_access_token()
        res1 = self.post_product(self.test_product, access_token=access_token)
        self.assertEqual(res1.status_code, 201)
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        res2 = self.client.delete(
            'api/v1/product/',
            data=self.test_product,
            headers=headers
        )
        self.assertEqual(res2.status_code, 202)
        self.assertIn('Deletion Successful', res2.json['message'])

    def deleting_non_existing_product(self):
        """Test deleting a non existing item"""
        access_token = self.get_user_access_token()
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        res = self.client.delete(
            'api/v1/product/',
            data=self.test_product,
            headers=headers
        )
        self.assertEqual(res.status_code, 400)
        self.assertIn(
            'Product {} not found'.format(self.test_product['p_name']),
            res.json['message']
        )
#

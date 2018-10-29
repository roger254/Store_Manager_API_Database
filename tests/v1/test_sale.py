import sys

import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from tests.v1.AppTest import AppBaseTest


class SaleTestCase(AppBaseTest):
    """Sale Test Case"""

    def post_sale(self, data, access_token=None):
        """POST a sale"""
        if access_token is None:
            access_token = self.get_user_access_token()
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        res1 = self.post_product(self.test_product)
        self.assertEqual(res1.status_code, 201)
        res = self.client.post(
            'api/v1/sales/',
            data=data,
            headers=headers
        )
        return res

    def test_sale_creation(self):
        """Test if user can make a sale"""
        access_token = self.get_user_access_token()
        res1 = self.post_product(self.test_product)
        self.assertEqual(res1.status_code, 201)

        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        res2 = self.client.post(
            'api/v1/sales/',
            data=self.test_sale,
            headers=headers
        )
        self.assertEqual(res2.status_code, 201)
        self.assertIn(
            self.test_sale['s_name'],
            res2.json['Sale']['s_name']
        )

    def test_missing_sale_name(self):
        """Test posting sale without sale name"""
        res = self.post_sale(self.missing_sale_name)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Sale name is required(s_name)', res.json['message'])

    def test_missing_sale_quantity(self):
        """Test post sale without sale quantity"""
        res = self.post_sale(self.missing_sale_quantity)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Sale quantity is required(s_quantity)', res.json['message'])

    def test_invalid_sale_quantity(self):
        """Test post sale with invalid quantity"""
        res = self.post_sale(self.invalid_sale_quantity)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Sale quantity(s_quantity) must be an int', res.json['message'])

    def test_invalid_sale_name(self):
        """Test post sale with invalid name"""
        res = self.post_sale(self.invalid_sale_name)
        self.assertEqual(res.status_code, 400)
        self.assertIn('Please enter a valid product name under (s_name)', res.json['message'])

    def test_unavailable_product_sale(self):
        """Test making sale of a non existing product"""
        res = self.post_sale(self.unavailable_product_sale)
        self.assertEqual(res.status_code, 404)
        self.assertIn(
            'Product {} not found'.format(self.unavailable_product_sale['s_name']),
            res.json['message']
        )

    def test_exceeding_sale_quantity(self):
        """Test post sale with exceeding quantity"""
        res = self.post_sale(self.sale_exceeding_product_quantity)
        self.assertEqual(res.status_code, 400)
        self.assertIn(
            'Sale quantity is more than the available quantity',
            res.json['message']
        )
        self.assertEqual(
            self.test_product['p_quantity'],
            res.json['Available Quantity']
        )

    def test_get_specific_sale(self):
        """Test user can get specific sale"""
        access_token = self.get_user_access_token()
        res = self.post_sale(self.test_sale, access_token=access_token)
        self.assertEqual(res.status_code, 201)

        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        res2 = self.client.get(
            'api/v1/sales/1',
            headers=headers
        )
        self.assertEqual(res2.status_code, 201)
        self.assertIn(
            self.test_sale['s_name'],
            res2.json['Sale']['s_name']
        )

    def test_unavailable_sale(self):
        """Test getting a non existing sale order"""
        access_token = self.get_user_access_token()
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        res = self.client.get(
            'api/v1/sales/1',
            headers=headers
        )
        self.assertEqual(res.status_code, 404)
        self.assertIn('Sale Order not found', res.json['message'])

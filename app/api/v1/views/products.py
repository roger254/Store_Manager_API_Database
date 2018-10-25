from flask import request, jsonify, make_response
from flask_classful import FlaskView, route

from .auth import authenticate
from ..models.items.product import Product

products = [
]


class ProductView(FlaskView):
    """Product View Class"""
    decorators = [authenticate]

    def index(self):
        if len(products) < 1:
            res = {
                'status': 'Failed',
                'message': 'No Products exits'
            }
            return res, 404
        response = {
            'status': 'Products Found',
            'products': list(map(f, products))
        }
        return response, 200

    def post(self, ):

        post_data = request.data
        # if it exists
        p_name = request.data['p_name']
        p_price = request.data['p_price']
        p_quantity = request.data['p_quantity']
        prod = Product(
            len(products) + 1,
            p_name,
            float(p_price),
            int(p_quantity)
        )
        invalid_product = prod.validate_data()
        if invalid_product:
            return make_response(jsonify(invalid_product)), 208
        for i in range(len(products)):
            if products[i].item_name == prod.item_price:
                message = {
                    'status': 'Adding Failed',
                    'message': 'Item Already Exists'
                }
                return make_response(jsonify(message)), 202
        else:
            if post_data:
                products.append(prod)
                # TODO: return product details
                return make_response(jsonify(prod.details())), 201

    @route('/<p_id>')
    def get(self, p_id):
        """Get item with id"""
        for i in range(len(products)):
            if products[i].item_id == int(p_id):
                product = products[i]
                return make_response(jsonify(product.details())), 200
        else:
            response = {
                'status': 'Failed',
                'message': 'Product Not Found'
            }
            return make_response(jsonify(response)), 404


def f(n):
    return n.details()

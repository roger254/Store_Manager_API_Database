from flask import request
from flask_classful import FlaskView, route
from flask_jwt_extended import jwt_required

from app.api.v1.views.auth import requires_admin
from .utils import Validate
from ..models.items.product import Products


class Product(FlaskView):
    """Product View Class"""
    decorators = [jwt_required]

    def index(self):
        """Get all products"""

        products = Products().fetch_all_products()

        if not products:
            return {
                       'message': "There are no products available"
                   }, 404
        return {
                   'Products': [product.serialize() for product in products]
               }, 200

    @requires_admin
    def post(self):
        """Create a new product"""
        product_data = request.data
        # if it exists
        if 'p_name' not in product_data:
            return {
                       'message': "Product name is required"
                   }, 400
        p_name = product_data['p_name']
        if 'p_price' not in product_data:
            return {
                       'message': "Product price is required"
                   }, 400
        p_price = product_data['p_price']
        if 'p_quantity' not in product_data:
            return {
                       'message': "Product quantity is required"
                   }, 400
        p_quantity = product_data['p_quantity']

        is_invalidate = Validate().is_input_valid(p_name)
        if is_invalidate:
            return {
                       'message': is_invalidate
                   }, 400

        # check if product exists
        product = Products().fetch_by_p_name(p_name=p_name)
        if product:
            return {
                       'message': 'Product already exist'
                   }, 400

        prod = Products(
            p_name=p_name,
            p_price=float(p_price),
            p_quantity=int(p_quantity)
        )
        prod.add()

        return {
                   'message': 'Product added',
                   'product': prod.serialize()
               }, 201

    @route('/<p_id>')
    def get(self, p_id):
        """Get item with id"""
        product = Products().fetch_by_id(id=p_id)
        if not product:
            return {
                       'message': 'Product does not exist'
                   }, 404
        return {
                   'Product': product.serialize()
               }, 201

    @route('/', methods=['PUT'])
    def put(self):
        """Update an item"""
        prod_data = request.data
        if 'p_name' not in prod_data:
            return {
                       'message': 'Product name is required(p_name)'
                   }, 400
        if 'p_price' not in prod_data:
            return {
                       'message': 'Product price(p_rice) required'
                   }, 400
        if 'p_quantity' not in prod_data:
            return {
                'message': 'Product quantity(p_quantity) required'
            }
        p_name = prod_data['p_name']
        product = Products().fetch_by_p_name(p_name)
        if not product:
            return {
                       'message': 'Product {} not found'.format(p_name)
                   }, 400

        p_price = prod_data['p_price']
        if p_price != product.p_price:
            product.p_price = p_price

        p_quantity = prod_data['p_quantity']
        if p_quantity != product.p_quantity:
            product.p_quantity = p_quantity

        product.update()
        return {
            'message': 'Product Successfully Update',
            'product': product.serialize()
        }

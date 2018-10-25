from flask_classful import FlaskView, route
from flask_jwt_extended import jwt_required
from flask_restful import reqparse

from app.api.v1.views.auth import requires_admin
from .utils import Validate
from ..models.items.product import Products


class ProductView(FlaskView):
    """Product View Class"""
    decorators = [jwt_required]

    parser = reqparse.RequestParser()
    parser.add_argument(
        'p_name',
        type=str,
        required=True,
        help='Product Name must be provided'
    )
    parser.add_argument(
        'p_price',
        type=float,
        required=True,
        help='Price should be a float value'
    )
    parser.add_argument(
        'p_quantity',
        type=int,
        required=True,
        help='Product quantity should an int'
    )

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
        product_data = ProductView.parser.parse_args()
        # if it exists
        p_name = product_data['p_name']
        p_price = product_data['p_price']
        p_quantity = product_data['p_quantity']
        is_invalidate = Validate.is_input_valid(p_name)
        if is_invalidate:
            return {
                       'message': 'Product name must be a string'
                   }, 400

        # check if product exists
        product = Products().fetch_by_p_name(p_name=p_name)
        if product:
            return {
                'message': 'Product already exist'
            }

        prod = Products(
            p_name=p_name,
            p_price=float(p_price),
            p_quantity=int(p_quantity)
        )
        prod.add()
        return {
            'message': 'Product added',
            'product': prod.serialize()
        }

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
        }

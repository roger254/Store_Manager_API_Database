from flask_classful import FlaskView, route
from flask_jwt_extended import jwt_required
from flask_restful import reqparse

from app.api.v1.models.items.product import Products
from app.api.v1.views.utils import Authentication
from app.api.v1.views.utils import Validate
from ..models.items.sale import Sales


class SaleView(FlaskView):
    """sale View Class"""

    decorators = [jwt_required]

    parser = reqparse.RequestParser()
    parser.add_argument(
        's_name',
        type=str,
        required=True,
        help='Sales Name must be provided'
    )
    parser.add_argument(
        's_quantity',
        type=int,
        required=True,
        help='Sale quantity must be provided'
    )

    @Authentication.requires_admin
    def index(self):
        # TODO: return valid response if none exists
        sales = Sales().fetch_all_sales()
        if not sales:
            return {
                       'message': 'No sales available'
                   }, 404
        return {
                   'Sales': [sale.serialize() for sale in sales]
               }, 200

    @Authentication.requires_user
    def post(self):
        """Post new sale"""
        sale_data = SaleView.parser.parse_args()
        s_name = sale_data['s_name']
        s_quantity = sale_data['s_quantity']

        invalid_sale_name = Validate().is_input_valid(s_name)
        if invalid_sale_name:
            return {
                       'message': invalid_sale_name
                   }, 400
        product = Products().fetch_by_p_name(s_name)
        if not product:
            return {
                       'message': 'Product {} not found'.format(s_name)
                   }, 404
        if product.p_quantity < s_quantity:
            return {
                       'message': "Sale quantity is more than the available quantity",
                       'Available Quantity': product.p_quantity
                   }, 400
        product.p_quantity -= s_quantity
        # update in database
        product.update()
        sale = Sales(
            s_name=s_name,
            s_price=product.p_price,
            s_quantity=s_quantity
        )
        sale.save()
        return {
                   'message': 'Sale Successful',
                   'Sale': sale.serialize()
               }, 201

    @route('/<id>')
    def get(self, id):
        """Get sale with id"""
        sale = Sales().fetch_by_id(id=id)
        if not sale:
            return {
                       'message': 'Sale Order not found'
                   }, 404
        return {
                   'Sale': sale.serialize()
               }, 201

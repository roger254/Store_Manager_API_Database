from flask import request
from flask_classful import FlaskView, route
from flask_jwt_extended import jwt_required

from app.api.v1.models.items.product import Products
from app.api.v1.views.utils import Authentication
from app.api.v1.views.utils import Validate
from ..models.items.sale import SalesModel


class Sales(FlaskView):
    """sale View Class"""

    decorators = [jwt_required]

    @Authentication.requires_admin
    def index(self):
        # TODO: return valid response if none exists
        sales = SalesModel().fetch_all_sales()
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
        sale_data = request.data

        if 's_name' not in sale_data:
            return {
                       'message': "Sale name is required(s_name)"
                   }, 400
        s_name = sale_data['s_name']

        if 's_quantity' not in sale_data:
            return {
                       'message': "Sale quantity is required(s_quantity)"
                   }, 400
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
        sale = SalesModel(
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

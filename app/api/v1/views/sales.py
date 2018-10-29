from flask import request
from flask_classful import FlaskView, route
from flask_jwt_extended import jwt_required

from app.api.v1.models.items.product import Products
from app.api.v1.views.utils import Validate
from ..models.items.sale import SalesModel


class Sales(FlaskView):
    """sale View Class"""

    decorators = [jwt_required]

    # @Authentication.requires_admin
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

    # @Authentication.requires_user
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
        try:
            s_quantity = int(s_quantity)
        except ValueError:
            return {
                       'message': 'Sale quantity(s_quantity) must be an int'
                   }, 400
        invalid_sale_name = Validate().is_string(s_name)
        if not invalid_sale_name:
            return {
                       'message': 'Please enter a valid product name under (s_name)'
                   }, 400
        product = Products().fetch_by_p_name(s_name)
        if not product:
            return {
                       'message': 'Product {} not found'.format(s_name)
                   }, 404
        if product.p_quantity < int(s_quantity):
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
        sale.add()
        return {
                   'message': 'Sale Successful',
                   'Sale': sale.serialize()
               }, 201

    @route('/<s_id>')
    def get(self, s_id):
        """Get sale with id"""
        sale = SalesModel().fetch_by_id(id=s_id)
        if not sale:
            return {
                       'message': 'Sale Order not found'
                   }, 404
        return {
                   'Sale': sale.serialize()
               }, 201

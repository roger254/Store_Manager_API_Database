# from flask import request, jsonify, make_response
# from flask_classful import FlaskView, route
#
# from .auth import authenticate
# from ..models.items.sale import Sale
# from ..views.products import products
#
# sales = [
# ]
#
#
# class SaleView(FlaskView):
#     """Product View Class"""
#     decorators = [authenticate]
#
#     def index(self):
#         # TODO: return valid response if none exists
#         response = {
#             'status': 'Items Found',
#             'sales': list(map(f, sales))
#         }
#         return response, 201
#
#     def post(self, ):
#
#         # if it exists
#         s_name = request.data['s_name']
#         s_quantity = request.data['s_quantity']
#
#         for i in range(len(products)):
#             if products[i].item_name == s_name:
#                 if products[i].item_quantity > s_quantity:
#                     products[i].item_quantity -= s_quantity
#                     sale = Sale(
#                         len(sales) + 1,
#                         s_name,
#                         float(s_price),
#                         int(s_quantity),
#                         'User 3'
#                     )
#                     invalid_product = sale.validate_data()
#                     if invalid_product:
#                         return make_response(jsonify(invalid_product)), 208
#                     sales.append(sale)
#                     # TODO: return product details
#                     return make_response(jsonify(sale.details())), 201
#                 else:
#                     res = {
#                         'message': 'Item quantity is lesser',
#                         'Actual Quantity': products[i].item_quantity
#                     }
#                     return res, 404
#         else:
#             res = {
#                 'message': 'Product not found'
#             }
#             return res, 404
#
#     @route('/<p_id>')
#     def get(self, p_id):
#         """Get item with id"""
#         for i in range(len(sales)):
#             if sales[i].item_id == int(p_id):
#                 sale = sales[i]
#                 return make_response(jsonify(sale.details())), 200
#         else:
#             response = {
#                 'status': 'Failed',
#                 'message': 'Sale Item Not Found'
#             }
#             return make_response(jsonify(response)), 404
#
#
# def f(n):
#     return n.details()

from flask import request
from flask_classful import FlaskView

from app.api.v1.models.user.user import User
from app.api.v1.views.utils import Validate


class Register(FlaskView):
    """Register a new user"""

    def post(self):
        """Create the user"""
        user_data = request.data

        if 'username' not in user_data:
            return {
                       'message': "Username must be provided"
                   }, 400
        username = user_data['username']

        if 'password' not in user_data:
            return {
                       'message': "Password must be provided"
                   }, 400
        password = user_data['password']

        invalid_username = Validate().is_input_valid(username)
        if invalid_username:
            return {
                       'message': invalid_username
                   }, 400

        invalid_password = Validate().is_password_valid(password)
        if invalid_password:
            return {
                       'message': invalid_password
                   }, 400

        if User().fetch_by_username(username):
            return {
                       'message': 'User {} already exists'.format(username)
                   }, 401

        user = User(username=username, password=password)
        user.add()

        return {
                   'message': 'User successfully added',
                   'user': user.serialize()
               }, 201

import datetime
from flask import request
from flask_classful import FlaskView
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.api.v1.models.user.user import User
from app.api.v1.views.utils import Validate


class Login(FlaskView):
    """Login a user"""

    def post(self):
        """Login the user"""

        user_data = request.data
        if 'username' not in user_data:
            return {
                       'message': "Username is required"
                   }, 400
        username = user_data['username']
        if len(username) < 6:
            return {
                       'message': "Username must be atleast 6 characters long"
                   }, 400

        if 'password' not in user_data:
            return {
                       'message': 'Password is required'
                   }, 400
        password = user_data['password']
        if len(password) < 6:
            return {
                       'message': "Password must be atleast 6 characters long"
                   }, 400

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

        user = User().fetch_by_username(username)
        if not user:
            return {
                       'message': 'User not found'
                   }, 404

        if not check_password_hash(user.hashed_password, password):
            return {
                       'message': 'Password is incorrect'
                   }, 400
        exp = datetime.timedelta(minutes=20)
        access_token = create_access_token(
            identity=user.serialize(),
            expires_delta=exp
        )
        # refresh_token = create_refresh_token(
        #     identity=user.serialize(),
        #     expires_delta=exp
        # )
        # response = jsonify({'login': True})
        # set_access_cookies(response, access_token)
        # set_refresh_cookies(response, refresh_token)

        return {
                   'message': 'Successfully logged in.',
                   'access_token': access_token
               }, 200

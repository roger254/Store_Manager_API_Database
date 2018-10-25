import datetime
from flask_classful import FlaskView
from flask_jwt_extended import create_access_token
from flask_restful import reqparse
from werkzeug.security import check_password_hash

from app.api.v1.models.user.user import User
from app.api.v1.views.utils import Validate


class Register(FlaskView):
    """Register a new user"""
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='Username is required'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='Password is required'
    )

    def post(self):
        """Create the user"""
        user_data = Register().parser.parse_args(strict=True)
        username = user_data['username']
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
            }

        user = User(username=username, password=password)
        user.add()

        return {
            'message': 'User successfully added',
            'user': user.serialize()
        }


class Login(FlaskView):
    """Login a user"""
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="Provide a valid username"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="Provide a valid password"
    )

    def post(self):
        """Login the user"""
        user_data = Login.parser.parse_args()
        username = user_data['username']
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

        user = User().fetch_by_username(username)
        if not user:
            return {
                       'message': 'User not found'
                   }, 404

        if not check_password_hash(user.password_hash, password):
            return {
                       'message': 'Password is incorrect'
                   }, 401
        exp = datetime.timedelta(minutes=20)
        token = create_access_token(
            identity=user.serialize(),
            expires_delta=exp
        )
        return {
                   'message': 'Successfully logged in.',
                   'access_token': token
               }, 200

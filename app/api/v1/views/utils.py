import re
from flask_jwt_extended import get_jwt_identity
from functools import wraps

from app.api.v1.models.user.user import User


class Authentication:

    @staticmethod
    def requires_admin(f):
        """Admin access only"""

        @wraps(f)
        def wrapper(*args, **kwargs):
            user = User().fetch_by_username(get_jwt_identity()['username'])
            if not user.is_admin:
                return {
                           'status': 'Unauthorized',
                           'message': "User must be admin"
                       }, 401
            return f(*args, **kwargs)

        return wrapper

    @staticmethod
    def requires_user(f):
        """Admin access only"""

        @wraps(f)
        def wrapper(*args, **kwargs):
            user = User().fetch_by_username(get_jwt_identity()['username'])
            if user.is_admin:
                return {
                           'status': 'Unwanted Access',
                           'message': "User must be Attendant"
                       }, 401
            return f(*args, **kwargs)

        return wrapper


class Validate:

    @staticmethod
    def is_input_valid(name):
        error = {}
        valid = re.match("^[a-zA-Z0-9_.-]{6,25}$", name)
        if valid is None:
            error['message'] = "Please enter a valid name"
        return error

    @staticmethod
    def is_password_valid(password):
        """Validate the password"""
        error = {}
        valid = re.match("[A-Za-z0-9@#$%^&+=]{8,}", password)
        if valid is None:
            error['message'] = "Please enter a valid password"
        return error

    @classmethod
    def is_string(cls, username):
        """Test if username is a string"""
        try:
            int(username)
        except ValueError:
            return True
        return False

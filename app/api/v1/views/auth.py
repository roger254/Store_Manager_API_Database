from flask_jwt_extended import get_jwt_identity
from functools import wraps

from app.api.v1.models.user.user import User


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

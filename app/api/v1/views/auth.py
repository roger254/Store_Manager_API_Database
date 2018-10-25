from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import request, make_response, jsonify

# env secret
FLASK_SECRET = 'to be changed'


def generate_user_token(user_id):
    """Generate access token for user using the id"""
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(minutes=10),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        access_token = jwt.encode(
            payload,
            FLASK_SECRET,
            algorithm='HS256'
        )
        return access_token
    except Exception as e:
        # Return the error message as string
        return str(e)


def decode_token(token):
    """Decodes the access token """
    try:
        #  decode the token using our secret var
        payload = jwt.decode(token, FLASK_SECRET)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        # the token is expired
        return "Expired token. Please login to get a new token"
    except jwt.InvalidTokenError:
        # the token is invalid, return an error string
        return "Invalid token. Please register or login"


def authenticate(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        access_token = auth_header.split(" ")[1]
        if access_token:
            user_id = decode_token(access_token)
            if not isinstance(user_id, str):
                return f(*args, **kwargs)
            else:
                message = user_id
                response = {
                    'status': 'failed',
                    'message': message
                }
                return make_response(jsonify(response))

    return wrapped

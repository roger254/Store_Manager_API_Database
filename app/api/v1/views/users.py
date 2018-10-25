from flask import request, jsonify, make_response
from flask_classful import FlaskView, route

from app.api.v1.models.user.regular import Regular
from .auth import generate_user_token

users = [
    Regular(1, 'Attendant 1', 'attpass1'),
    Regular(2, 'Attendant 2', 'attpass2'),
    Regular(3, 'Attendant 3', 'attpass3'),
    Regular(4, 'Attendant 4', 'attpass4')
]


class UserView(FlaskView):
    """Product View Class"""

    @route('/register', methods=['POST'])
    def post(self):
        """Get user data"""
        post_data = request.data
        # if it exists
        user_name = request.data['user_name']
        password = request.data['password']
        user = Regular(
            len(users) + 1,
            user_name,
            password
        )
        invalid_user = user.validate_data()
        if invalid_user:
            return make_response(jsonify(invalid_user)), 208
        for i in range(len(users)):
            if users[i].user_name == user.user_name:
                message = {
                    'status': 'Registration Failed',
                    'message': 'User Exists. Please Log in!'
                }
                return make_response(jsonify(message)), 202
        else:
            if post_data:
                users.append(user)
                return make_response(jsonify(user.user_details())), 201

    @route('/login', methods=['POST'])
    def login(self):
        try:
            user = request.data['user_name']
            user_pass = request.data['password']
            for i in range(len(users)):
                if users[i].user_name == user and users[i].password == user_pass:
                    access_token = generate_user_token(users[i].user_id)
                    if access_token:
                        response = {
                            "message": "You've logged in successfully.",
                            "access_token": access_token.decode()
                        }

                        return make_response(jsonify(response)), 200
            else:
                response = {
                    "message": "Invalid username or password, Please try again"
                }
                return make_response(jsonify(response)), 401
        except Exception as e:
            response = {
                'message': str(e)
            }
            return make_response(jsonify(response)), 500

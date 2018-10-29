from flask import jsonify
from flask_api import FlaskAPI
from flask_jwt_extended import JWTManager, jwt_required, get_raw_jwt

from app.api.v1.views.login import Login
from app.api.v1.views.products import Product
from app.api.v1.views.register import Register
from app.api.v1.views.sales import Sales
from instance.config import app_config

jwt = JWTManager()


def create_app(config_name):
    """Create app"""
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
    jwt.init_app(app)

    blacklist = set()

    @jwt.revoked_token_loader
    def revoked_token():
        return jsonify({
            'Message': "User has been logged out, Please Log in"
        }), 400

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in blacklist

      
    @jwt.expired_token_loader
    def my_expired_token_callback():
        return jsonify({
            'Message': "You've been logged out"
        }), 400
    
    @jwt.invalid_token_loader
    def my_invalid_callback():
        return jsonify({
            'Message': "Please login with correct details"
        }), 400



    # Views
    Register.register(app, route_prefix='api/v1')
    Login.register(app, route_prefix='api/v1')
    Product.register(app, route_prefix='api/v1')
    Sales.register(app, route_prefix='api/v1')

    @app.route('/api/v1/logout', methods=['DELETE'])
    @jwt_required
    def logout():
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        return jsonify({"msg": "Successfully logged out"}), 200

    return app

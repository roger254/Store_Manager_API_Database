from flask_api import FlaskAPI
# from flask_cors import CORS
from flask_jwt_extended import JWTManager

from app.api.v1.views.products import Product
from app.api.v1.views.sales import Sales
from app.api.v1.views.register import Register
from app.api.v1.views.login import Login
from instance.config import app_config

jwt = JWTManager()


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    jwt.init_app(app)
    # CORS(app)

    # Views
    Register.register(app, route_prefix='api/v1')
    Login.register(app, route_prefix='api/v1')
    Product.register(app, route_prefix='api/v1')
    Sales.register(app, route_prefix='api/v1')

    return app

from flask_api import FlaskAPI
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from app.api.v1.views.products import ProductView
from app.api.v1.views.sales import SaleView
from app.api.v1.views.users import Register, Login
from instance.config import app_config

jwt = JWTManager()


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    jwt.init_app(app)
    CORS(app)

    # Views
    Register.register(app, route_prefix='/api/v1')
    Login.register(app, route_prefix='api/v1')
    ProductView.register(app, route_prefix='api/v1')
    SaleView.register(app, route_base='/api/v1')

    return app

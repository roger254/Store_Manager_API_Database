from flask_api import FlaskAPI

from app.api.v1.views.products import ProductView
from app.api.v1.views.sales import SaleView
from app.api.v1.views.users import UserView
from instance.config import app_config


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # Views

    ProductView.register(app, route_base='/products/')
    SaleView.register(app, route_base='/sales/')
    UserView.register(app, route_base='/users/')
    return app

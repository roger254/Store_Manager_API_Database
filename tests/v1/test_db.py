from app import create_app

from app.api.v1.models.items.product import Product
from app.api.v1.models.items.sale import Sale
from app.api.v1.models.user.user import User

app = create_app('testing')


def migrate():
    """create tables """
    User.create_user_table()
    Product.create_product_table()
    Sale.create_sale_table()


def drop():
    """Drop all test tables"""
    User.drop()
    Product.drop()
    Sale.drop()


def create_admin_user():
    """create test admin"""
    admin = User(username='root', password='root1234', is_admin=True)
    admin.add()

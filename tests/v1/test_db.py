from app import create_app

from app.api.v1.models.items.product import Products
from app.api.v1.models.items.sale import SalesModel
from app.api.v1.models.user.user import User

app = create_app('testing')


def migrate():
    """create tables """
    User().create_user_table()
    Products().create_product_table()
    SalesModel().create_sales_table()


def drop():
    """Drop all test tables"""
    User().drop()
    Products().drop()
    SalesModel().drop()


def create_admin_user():
    """create test admin"""
    admin = User(username='root254', password='root1234', is_admin=True)
    admin.add()

from app import create_app
from app.api.v1.models import ProductDB, SaleDB, UserDB

app = create_app('testing')


def migrate():
    """create tables """
    UserDB.create()
    ProductDB.create()
    SaleDB.create()


def drop():
    """Drop all test tables"""
    UserDB.drop()
    ProductDB.drop()
    SaleDB.drop()


def create_admin_user():
    """create test admin"""
    admin = User(user_name='root', password='root1234', is_admin=True)
    admin.add()

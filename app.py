import os

from app import create_app
from app.api.v1.models.items.product import Products
from app.api.v1.models.items.sale import SalesModel
from app.api.v1.models.user.user import User

app = create_app(os.getenv('FLASK_ENV') or 'default')


@app.cli.command()
def migrate():
    User().create_user_table()
    Products().create_product_table()
    SalesModel().create_sales_table()


@app.cli.command()
def drop():
    User().drop()
    Products().drop()
    SalesModel().drop()


@app.cli.command()
def default_admin():
    user = User(
        username='Admin254',
        password='testadmin123',
        is_admin=True
    )
    user.add()


# run app
if __name__ == '__main__':
    app.run(port=8000)

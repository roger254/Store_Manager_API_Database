from datetime import datetime

from app.api.v1.models.base_model import BaseDatabase


class Product(BaseDatabase):
    """Represents the  Product Model"""

    def __init__(self, p_name=None, p_price=None, p_quantity=None):
        super().__init__()
        self.p_name = p_name
        self.p_price = p_price
        self.p_quantity = p_quantity
        self.date = datetime.now().replace(second=0, microsecond=0)

    def create_product_table(self):
        """Create product table"""
        self.create_table(
            """
            CREATE TABLE IF NOT EXIST products (
            id serial PRIMARY KEY,
            p_name VARCHAR NOT NULL,
            p_price DOUBLE PRECISION,
            p_quantity INTEGER,
            date TIMESTAMP
            );
            """
        )

    def add(self):
        """add new product"""
        query = 'INSERT INTO products(p_name, p_price,p_quantity,date) VALUES (%s,%s,%s,%s)'
        data = (self.p_name, self.p_price, self.p_quantity, self.date)
        self.cur.execute(query, data)
        self.save()

    def map_product(self, data):
        """map to an object"""
        product = Product(
            p_name=data[1],
            p_price=data[2],
            p_quantity=data[3],
        )
        product.id = data[0]
        product.date = data[5]
        self = product
        return self

    def serialize(self):
        """Return data as dict"""
        return dict(
            id=self.id,
            p_name=self.p_name,
            p_price=self.p_price,
            p_quantity=self.p_quantity,
            date=self.date
        )

    def fetch_all_products(self):
        """Get all products"""
        self.cur.execute('SELECT * FROM products')
        products = self.cur.fetchall()
        self.save()
        self.close()

        if products:
            return [self.map_product(product) for product in products]
        return None

    def fetch_by_id(self, id):
        """fetch product by id"""
        self.cur.execute(
            "SELECT * FROM products where id = %s", (id,)
        )
        product = self.cur.fetchone()
        self.save()
        self.close()

        if product:
            return self.map_product(product)
        return None

    def fetch_by_p_name(self, p_name):
        """fetch product by id"""
        self.cur.execute(
            "SELECT * FROM products where p_name = %s", (p_name,)
        )
        product = self.cur.fetchone()
        self.save()
        self.close()

        if product:
            return self.map_product(product)
        return None

    def update(self, product_id):
        """Update an existing product"""
        self.cur.execute(
            "UPDATE products SET p_name = %s, p_price = %s, p_quantity = %s WHERE id = %s",
            (self.p_name, self.p_price, self.p_quantity)
        )
        self.save()
        self.close()

    def delete(self, product_id):
        """delete product"""
        self.cur.execute(
            "DELETE FROM products WHERE id = %s", (product_id,)
        )
        self.save()
        self.close()

    def drop(self):
        """Drop if it exists"""
        self.drop_table('products')

from datetime import datetime

from app.api.v1.models.base_model import BaseDatabase


class Sales(BaseDatabase):
    """Represents the  Product Model"""

    def __init__(self, s_name=None, s_price=None, s_quantity=None):
        super().__init__()
        self.s_name = s_name
        self.s_price = s_price
        self.s_quantity = s_quantity
        self.date = datetime.now().replace(second=0, microsecond=0)

    def create_sales_table(self):
        """Create product table"""
        self.create_table(
            """
            CREATE TABLE IF NOT EXIST sales (
            id serial PRIMARY KEY,
            s_name VARCHAR NOT NULL,
            s_price DOUBLE PRECISION,
            s_quantity INTEGER,
            date TIMESTAMP
            );
            """
        )

    def add(self):
        """add new sale"""
        query = 'INSERT INTO products(s_name, s_price,s_quantity,date) VALUES (%s,%s,%s,%s)'
        data = (self.s_name, self.s_price, self.s_quantity, self.date)
        self.cur.execute(query, data)
        self.save()

    def map_sale(self, data):
        """map to an object"""
        sale = Sales(
            s_name=data[1],
            s_price=data[2],
            s_quantity=data[3],
        )
        sale.id = data[0]
        sale.date = data[5]
        self = sale
        return self

    def serialize(self):
        """Return data as dict"""
        return dict(
            id=self.id,
            s_name=self.s_name,
            s_price=self.s_price,
            s_quantity=self.s_quantity,
            date=self.date
        )

    def fetch_all_sales(self):
        """Get all products"""
        self.cur.execute('SELECT * FROM sales')
        sales = self.cur.fetchall()
        self.save()
        self.close()

        if sales:
            return [self.map_sale(sale) for sale in sales]
        return None

    def fetch_by_id(self, id):
        """fetch product by id"""
        self.cur.execute(
            "SELECT * FROM sales where id = %s", (id,)
        )
        sale = self.cur.fetchone()
        self.save()
        self.close()

        if sale:
            return self.map_sale(sale)
        return None

    def fetch_by_s_name(self, s_name):
        """fetch product by id"""
        self.cur.execute(
            "SELECT * FROM products where s_name = %s", (s_name,)
        )
        sale = self.cur.fetchone()
        self.save()
        self.close()

        if sale:
            return self.map_sale(sale)
        return None

    def update(self, sale_id):
        """Update an existing product"""
        self.cur.execute(
            "UPDATE sale SET s_name = %s, s_price = %s, s_quantity = %s WHERE id = %s",
            (self.s_name, self.s_price, self.s_quantity, sale_id)
        )
        self.save()
        self.close()

    def delete(self, sale_id):
        """delete product"""
        self.cur.execute(
            "DELETE FROM products WHERE id = %s", (sale_id,)
        )
        self.save()
        self.close()

    def drop(self):
        """Drop if it exists"""
        self.drop_table('sales')

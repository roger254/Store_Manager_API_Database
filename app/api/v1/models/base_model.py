import psycopg2 as psycopg2
from flask import current_app


class BaseDatabase:
    """Design database model"""

    def __init__(self):
        self.db_host = current_app.config['DB_HOST']
        self.db_username = current_app.config['DB_USERNAME']
        self.db_password = current_app.config['DB_PASSWORD']
        self.db_name = current_app.config['DB_NAME']
        self.conn = psycopg2.connect(
            host=self.db_host,
            user=self.db_username,
            password=self.db_password,
            database=self.db_name
        )
        self.cur = self.conn.cursor()

    def create_table(self, schema):
        """Create database tables"""
        self.cur.execute(schema)
        self.save()

    def save(self):
        """Commit changes made"""
        self.conn.commit()

    def drop_table(self, name):
        """Drop existing table(testing)"""
        self.cur.execute("DROP TABLE IF EXISTS " + name)

    def close(self):
        """Close connection"""
        self.cur.close()

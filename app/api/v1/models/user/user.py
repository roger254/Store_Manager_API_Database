from werkzeug.security import generate_password_hash

from app.api.v1.models.base_model import BaseDatabase


class User(BaseDatabase):
    """Represents The User Model"""

    def __init__(self, username=None, password=None, is_admin=False):
        super().__init__()
        self.id = None
        self.username = username
        if password:
            self.hashed_password = generate_password_hash(password)
        self.is_admin = is_admin

    def create_user_table(self):
        """Create user table"""
        self.create_table(
            """
            CREATE TABLE IF NOT EXISTS users(
            id serial PRIMARY KEY,
            username VARCHAR NOT NULL,
            password VARCHAR NOT NULL,
            is_admin BOOLEAN NOT NULL
            );
            """
        )

    def add(self):
        """add new user"""
        query = "INSERT INTO users(username,password,is_admin) VALUES(%s,%s,%s)"
        data = (self.username, self.hashed_password, self.is_admin)
        self.cur.execute(query, data)
        self.save()

    def fetch_by_username(self, username):
        """Get user by username"""
        self.cur.execute(
            "SELECT * FROM users WHERE username=%s", (username,)
        )
        user = self.cur.fetchone()
        if user:
            return self.map_details(user)
        return None

    def map_details(self, data):
        """Create user from db data"""
        self.id = data[0]
        self.username = data[1]
        self.hashed_password = data[2]
        self.is_admin = data[3]
        return self

    def serialize(self):
        """Return user as a dict"""
        return dict(
            id=self.id,
            username=self.username,
            is_admin=self.is_admin
        )

    def drop(self):
        """Drop if it exists"""
        self.drop_table('users')

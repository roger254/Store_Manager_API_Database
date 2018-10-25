import datetime as date


class User:
    """Represents The User Model"""

    def __init__(self, user_id, user_name, password, user_type):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.user_type = user_type
        self.date_created = date.datetime.now()

    def validate_data(self):
        errors = []

        if len(self.user_name) < 8:
            errors.append("Username Must be at least 8 characters")
        if len(self.password) < 8:
            errors.append("Password must be at least 8 characters ")
        return errors

    def user_details(self):
        return dict(
            user_id=self.user_id,
            user_name=self.user_name,
            user_type=self.user_type
        )

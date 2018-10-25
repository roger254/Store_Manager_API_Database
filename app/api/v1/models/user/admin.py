from .user import User
from .user_type import UserType


class Admin(User):
    """Represents the Admin or Owner"""

    def __init__(self, user_id, user_name, password):
        super(Admin, self).__init__(user_id, user_name, password, 'ADMIN')

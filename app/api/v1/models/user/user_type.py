from enum import Enum


class UserType(Enum):
    _init_ = 'value string'

    ADMIN = 1, 'ADMIN'
    REGULAR = 2, 'REGULAR'

    def __str__(self):
        return self.string

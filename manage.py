import unittest
from flask_script import Manager

from app import create_app
# import user model
from app.api.v1.models.user.user import User

app = create_app('testing')

# for  running commands on terminal
manager = Manager(app)


# define our command for testing called "test"
# Usage: python manage.py test
@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('./tests/v1/', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


# usage python manage.py migrate
@manager.command
def migrate():
    user = User()
    user.create_user_table()


# usage python manage.py create_admin
@manager.command
def create_admin():
    """ add admin """
    user = User(username='admin',
                password='root2454', is_admin=True)
    user.add()


if __name__ == '__main__':
    manager.run()

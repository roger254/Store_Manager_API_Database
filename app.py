from app import create_app
from app.api.v1.models.user.user import User

app = create_app('testing')


@app.cli.command()
def migrate():
    User().create_user_table()


@app.cli.command()
def create_admin():
    """ add admin """
    user = User(username='admin',
                password='root2454', is_admin=True)
    user.add()


if __name__ == '__main__':
    app.run(port=8080)

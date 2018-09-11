from flaskr import create_app
from flaskr import db
from flask_script import Manager, commands
from flask_migrate import Migrate, MigrateCommand
# from flask_admin import Admin, AdminIndexView

app = create_app()


def create_db():
    db.create_all()


app.before_first_request(create_db)


manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def hello():
    print("hello")


if __name__ == '__main__':
    manager.run()



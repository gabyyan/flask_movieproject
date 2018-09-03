from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)

    from flaskr.home import homes
    from flaskr.admin import admins
    app.register_blueprint(homes)
    app.register_blueprint(admins)

    csrf = CSRFProtect()
    csrf.init_app(app)
    db.init_app(app)

    return app

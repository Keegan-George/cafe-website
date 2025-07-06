from os import urandom
from flask import Flask
from models import db
from blueprints.add import add_bp
from blueprints.view import view_bp
from blueprints.delete import delete_bp


def create_app():
    # create flask app
    app = Flask(__name__)

    # configure SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"

    # set secret key for csrf protection in flask form
    app.config["SECRET_KEY"] = urandom(32)

    # initialize the app with the extension
    db.init_app(app)

    # create table schema in the database
    with app.app_context():
        db.create_all()

    app.register_blueprint(add_bp)
    app.register_blueprint(view_bp)
    app.register_blueprint(delete_bp)

    return app

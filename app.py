from os import getenv
from flask import Flask
from dotenv import load_dotenv
from models import db
from blueprints.add import add_bp
from blueprints.view import view_bp
from blueprints.delete import delete_bp


def create_app():
    # load environment variables
    load_dotenv()

    # create flask app
    app = Flask(__name__)

    # configure SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL", "sqlite:///cafes.db")

    # set secret key
    app.config["SECRET_KEY"] = getenv("SECRET_KEY", "fallback-secret-key")

    # initialize the app with the extension
    db.init_app(app)

    # create table schema in the database
    with app.app_context():
        db.create_all()

    app.register_blueprint(add_bp)
    app.register_blueprint(view_bp)
    app.register_blueprint(delete_bp)

    return app

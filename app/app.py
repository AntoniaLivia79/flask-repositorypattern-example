from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import get_config

db = SQLAlchemy()


def create_app(env='development'):
    app = Flask(__name__)
    app.config.from_object(get_config(env))
    # Set up SQLAlchemy database connection
    db.init_app(app)
    return app
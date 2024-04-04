from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import UserModel

__all__ = ['UserModel']

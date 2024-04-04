from . import db


class UserModel(db.Model):

    __tablename__ = 'users'

    username = db.Column(
        db.String, primary_key=True,
        unique=True, nullable=False)
    country = db.Column(
        db.String, nullable=False)

    def __init__(self, username: str, country: str):
        self.username = username
        self.country = country

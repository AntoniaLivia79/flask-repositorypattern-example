from flask_restful import Resource

from app.repositories import UserRepository


class User(Resource):
    def get(self, username: str):
        user = UserRepository.get(username)
        return user, 200
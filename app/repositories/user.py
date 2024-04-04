from app.models import UserModel


class UserRepository:

    @staticmethod
    def get(username: str) -> dict:
        """ Query a user by username """
        user = UserModel.query.filter_by(username=username).first_or_404()
        user = {
          'username': user.username,
          'country': user.country
        }
        return user

from flask_restful import Api
from app.resources import HealthCheck, User
from app.app import create_app

app = create_app()

# API
api = Api(app)
api.add_resource(HealthCheck, '/healthcheck')
api.add_resource(User, '/api/users/<username>')


from flask import Blueprint
from src.controllers.users import users
from src.controllers.client import clients

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(users, url_prefix="/users")
api.register_blueprint(clients, url_prefix="/clients")
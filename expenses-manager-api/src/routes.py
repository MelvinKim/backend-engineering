from flask import Blueprint
from src.controllers.users import users
from src.controllers.client import clients
from src.controllers.account import accounts
from src.controllers.transaction import transactions

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(users, url_prefix="/users")
api.register_blueprint(clients, url_prefix="/clients")
api.register_blueprint(accounts, url_prefix="/accounts")
api.register_blueprint(transactions, url_prefix="/transactions")
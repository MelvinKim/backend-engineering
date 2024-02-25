from flask import Flask
import os
from src.config.config import Config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# load env variables
load_dotenv()

# declare flask app
app = Flask(__name__)

# call the dev config
config = Config().dev_config

# make the app to use dev env
app.env = config.ENV

# Path for our local sql lite database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")

# sqlachemy instance
db = SQLAlchemy(app)

# Flask Migrate instance to handle migrations
migrate = Migrate(app, db)

# import models to let the migrate tool know
from src.models.account import Account
from src.models.client import Client
from src.models.transaction import Transaction

# import api blueprint to register it with app
from src.routes import api
app.register_blueprint(api, url_prefix = "/api")

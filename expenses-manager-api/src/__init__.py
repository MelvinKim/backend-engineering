from flask import Flask
import os
from src.config.config import Config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.pool import NullPool
import redis

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
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'poolclass': NullPool,
}

# redis configuration
cache = redis.Redis(
    host=os.environ.get("CACHE_REDIS_HOST", "localhost"),
    db=os.environ.get("CACHE_REDIS_DB", 1),
    port=os.environ.get("CACHE_REDIS_PORT", 6379),
    password=os.environ.get("CACHE_REDIS_PASSWORD", None),
    charset="utf-8",
    decode_responses=True
)

# sqlachemy instance
db = SQLAlchemy(app)
with app.app_context():
    engine_container = db.get_engine(app, bind=None)

# Flask Migrate instance to handle migrations
migrate = Migrate(app, db)

# import models to let the migrate tool know
from src.models.account import Account
from src.models.client import Client
from src.models.transaction import Transaction

# import api blueprint to register it with app
from src.routes import api
app.register_blueprint(api, url_prefix = "/api")

from src.utils.common import cleanup
@app.after_request
def after_request(response):
    cleanup(db.session)
    return response

from src.boot.on_boot import run_all
run_all(app)
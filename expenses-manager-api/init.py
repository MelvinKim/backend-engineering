from flask import Flask
import os
from src.config.config import Config
from dotenv import load_dotenv

# load env variables
load_dotenv()

# declare flask app 
app = Flask(__name__)

# call the dev config
config = Config().dev_config

# make the app to use dev env
app.env = config.ENV
from celery import Celery
from src import app

with app.app_context():
    celery = Celery(main='tasks',broker='amqp://celery_1:celery_1@localhost:5672')
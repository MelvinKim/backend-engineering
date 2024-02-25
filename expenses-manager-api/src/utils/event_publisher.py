import pika
import uuid
import os

from pika.exceptions import ConnectionClosed, ChannelClosed

from src import app
from src.constants.pub_sub_constants import EVENTS_GLOBAL_TASK_NAME, EXCHANGE_QUEUE_BINDING, \
    DIRECT_QUEUE_ROUTING


class EventPublisher:

    def __init__(self, host=None, port=None, vhost=None, user=None, password=None):
        host = os.getenv("RABBIMQ_HOST", "host")
        port = os.getenv("RABBIMQ_PORT", "5672")
        vhost = os.getenv("RABBIMQ_VHOST")
        user = os.getenv("RABBITMQ_USER")
        password = os.getenv("RABBITMQ_PASSWORD")
        credentials = pika.PlainCredentials(user, password)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host,
                                      port=port,
                                      credentials=credentials,
                                      virtual_host=vhost,
                                      heartbeat=0)
        )
        self.connection = connection
        self.channel = connection.channel()

    @staticmethod
    def format_publish_message(message, exchange, task=EVENTS_GLOBAL_TASK_NAME) -> dict:
        id = str(uuid.uuid4())
        return dict(exchange=exchange,
                    routing_key="", # TODO
                    body=message,
                    properties=pika.spec.BasicProperties(
                        headers=dict(task=task, id=id),
                        content_type='application/json'
                    )
                    )

    def exchange_queue_binding(self):
        for exchange in EXCHANGE_QUEUE_BINDING:
            self.channel.exchange_declare(exchange=exchange.get('exchange'),
                                          exchange_type=exchange.get('type'),
                                          durable=True)
            for queue in exchange.get('queues', []):
                routing_key = DIRECT_QUEUE_ROUTING[exchange.get('exchange')] if exchange.get('type') == DIRECT else ''
                self.channel.queue_declare(queue=queue, durable=True)
                self.channel.queue_bind(exchange=exchange.get('exchange'), queue=queue,
                                        routing_key=routing_key)

    def publish_message(self, message, exchange, task, id=None):
        try:
             self.channel.basic_publish(**EventPublisher.format_publish_message(message, exchange=exchange, task=task))
             app.logger.info(f"Sent message {message} to {exchange}")
        except (ConnectionClosed, ChannelClosed) as e:
            app.logger(f"Error {e} on tring to send message {message} to {exchange}")
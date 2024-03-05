from src.workers.celery_app import celery
from src.utils.event_publisher import EventPublisher
from src.constants.pub_sub_constants import ACCOUNTS_RABBIT_MQ_QUEUE_NAME
import time

# def process_message(channel, method, properties, body):
#     print(" Received: %r" % body)

@celery.task
def create_account():
    time.sleep(6)
    print('Hi there')
    # conn = EventPublisher().connection
    # channel = EventPublisher().channel

    # try:
    #     time.sleep(5)
    #     print('Hi, new message')
    #     channel.basic_consume(queue=ACCOUNTS_RABBIT_MQ_QUEUE_NAME, on_message_callback=process_message, auto_ack=True)
    #     channel.start_consuming()
    #     conn.process_data_events(time_limit=0)
    # finally:
    #     conn.close()
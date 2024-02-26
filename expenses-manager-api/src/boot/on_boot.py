from src.utils.event_publisher import EventPublisher

def run_all(app):
    publisher = EventPublisher()
    publisher.exchange_queue_binding()
    
    app.logger.info("Initializing rabbitmq")
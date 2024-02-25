import os


# Exchanges for PUB SUB
EVENTS_RABBIT_MQ_EXCHANGE_NAME = 'agent_events'
AGENT_SHOP_ONBOARDING_EXCHANGE = 'agent_shop_onboarding'
INVOICE_AGENT_EVENTS_EXCHANGE = 'invoice_agent_events'
SHOP_CACHE_CONSTRUCTOR_EXCHANGE = 'shop_cache_constructor_exchange'
AGENT_PRODUCT_REORDERING_RULE_EXCHANGE = "agent_product_reordering_rules"
AGENT_SASA_SHOP_EVENT_QUEUE_NAME = 'agent_sasa_shop_event_queue'

# Exchange types
FANOUT = "fanout"
DIRECT = "direct"

EXCHANGE_QUEUE_BINDING = [
    dict(
        exchange=EVENTS_RABBIT_MQ_EXCHANGE_NAME,
        queues=[os.getenv('EVENTS_AGENT_QUEUE_NAME'),
                os.getenv('EVENTS_COP_QUEUE_NAME'),
                os.getenv('AGENT_SASA_SHOP_EVENT_QUEUE_NAME'),
                os.getenv('EVENTS_RETAIL_QUEUE_NAME')],
        type=FANOUT
    ),
    dict(
        exchange=AGENT_SHOP_ONBOARDING_EXCHANGE,
        queues=[os.getenv('AGENT_INVOICE_EVENTS_QUEUE_NAME')],
        type=FANOUT
    ),
    dict(
        exchange=INVOICE_AGENT_EVENTS_EXCHANGE,
        queues=[os.getenv('INVOICE_AGENT_EVENTS_QUEUE_NAME')],
        type=DIRECT
    ),
    dict(
        exchange=AGENT_PRODUCT_REORDERING_RULE_EXCHANGE,
        queues=[os.getenv('AGENT_ERP_PRODUCT_REORDERING_RULE_QUEUE')],
        type=FANOUT
    ),
    dict(
        exchange=SHOP_CACHE_CONSTRUCTOR_EXCHANGE,
        queues=[os.getenv('PGAMQP_EVENTS_QUEUE_NAME')],
        type=DIRECT
    )
]

DIRECT_QUEUE_ROUTING = {
    SHOP_CACHE_CONSTRUCTOR_EXCHANGE: os.getenv('PGAMQP_EVENTS_QUEUE_NAME'),
    INVOICE_AGENT_EVENTS_EXCHANGE: os.getenv('INVOICE_AGENT_EVENTS_QUEUE_NAME'),
    AGENT_SASA_SHOP_EVENT_QUEUE_NAME: os.getenv('AGENT_SASA_SHOP_EVENT_QUEUE_NAME')
}
import os


# Exchanges for PUB SUB
EXPENSES_RABBIT_MQ_EXCHANGE_NAME = 'expenses_events'
EXPENSES_RABBIT_MQ_QUEUE_NAME = "expenses"
EXPENSES_TASK_NAME = "expenses"
EVENTS_GLOBAL_TASK_NAME = "events_task_worker"

# Exchange types
FANOUT = "fanout"
DIRECT = "direct"

EXCHANGE_QUEUE_BINDING = [
    dict(
        exchange=EXPENSES_RABBIT_MQ_EXCHANGE_NAME,
        queues=[EXPENSES_RABBIT_MQ_QUEUE_NAME],
        type=FANOUT
    )
]

DIRECT_QUEUE_ROUTING = {
    EXPENSES_RABBIT_MQ_EXCHANGE_NAME: EXPENSES_RABBIT_MQ_QUEUE_NAME
}
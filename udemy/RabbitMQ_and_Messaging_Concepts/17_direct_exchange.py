from pika.exchange_type import ExchangeType

from utilts import *


EXCHANGE = 'ex.direct'
QUEUE_INFOS = 'queue.infos'
QUEUE_WARNINGS = 'queue.warnings'
QUEUE_ERRORS = 'queue.errors'
ROUTING_KEY_INFO = 'info'
ROUTING_KEY_WARNING = 'warning'
ROUTING_KEY_ERROR = 'error'

with get_channel() as channel:
    channel.exchange_declare(EXCHANGE, ExchangeType.direct)
    channel.queue_declare(QUEUE_INFOS)
    channel.queue_declare(QUEUE_WARNINGS)
    channel.queue_declare(QUEUE_ERRORS)
    channel.queue_bind(QUEUE_INFOS, EXCHANGE, ROUTING_KEY_INFO)
    channel.queue_bind(QUEUE_WARNINGS, EXCHANGE, ROUTING_KEY_WARNING)
    channel.queue_bind(QUEUE_ERRORS, EXCHANGE, ROUTING_KEY_ERROR)

    channel.basic_publish(EXCHANGE, ROUTING_KEY_INFO, 'Message info')
    channel.basic_publish(EXCHANGE, ROUTING_KEY_WARNING, 'Message warning')
    channel.basic_publish(EXCHANGE, ROUTING_KEY_ERROR, 'Message error')

    show_message(channel, QUEUE_INFOS, *channel.basic_get(QUEUE_INFOS))
    show_message(channel, QUEUE_WARNINGS, *channel.basic_get(QUEUE_WARNINGS))
    show_message(channel, QUEUE_ERRORS, *channel.basic_get(QUEUE_ERRORS))

    channel.queue_delete(QUEUE_INFOS)
    channel.queue_delete(QUEUE_WARNINGS)
    channel.queue_delete(QUEUE_ERRORS)
    channel.exchange_delete(EXCHANGE)


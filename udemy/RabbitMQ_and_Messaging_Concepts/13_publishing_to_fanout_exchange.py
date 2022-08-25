from pika.exchange_type import ExchangeType

from utils import *

EXCHANGE = 'ex.fanout'
QUEUE1 = 'my.queue1'
QUEUE2 = 'my.queue2'
ROUTING_KEY = ''

with get_channel() as channel:
    channel.exchange_declare(EXCHANGE, ExchangeType.fanout)
    channel.queue_declare(QUEUE1)
    channel.queue_declare(QUEUE2)
    channel.queue_bind(QUEUE1, EXCHANGE, ROUTING_KEY)
    channel.queue_bind(QUEUE2, EXCHANGE, ROUTING_KEY)

    channel.basic_publish(EXCHANGE, ROUTING_KEY, 'Message 1')
    channel.basic_publish(EXCHANGE, ROUTING_KEY, 'Message 2')

    for _ in range(3):
        show_message(channel, QUEUE1, *channel.basic_get(QUEUE1))
    for _ in range(3):
        show_message(channel, QUEUE2, *channel.basic_get(QUEUE2))

    channel.queue_delete('my.queque1')
    channel.queue_delete('my.queque2')
    channel.exchange_delete('ex.fanout')


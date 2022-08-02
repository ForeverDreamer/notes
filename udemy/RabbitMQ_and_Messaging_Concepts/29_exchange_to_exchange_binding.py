from pika.exchange_type import ExchangeType

from utils import *

EXCHANGE1 = 'exchange1'
EXCHANGE2 = 'exchange2'
QUEUE1 = 'queue1'
QUEUE2 = 'queue2'
KEY1 = 'key1'
KEY2 = 'key2'


with get_channel() as channel:
    channel.exchange_declare(EXCHANGE1, ExchangeType.direct)
    channel.exchange_declare(EXCHANGE2, ExchangeType.direct)
    channel.queue_declare(QUEUE1)
    channel.queue_declare(QUEUE2)

    channel.queue_bind(QUEUE1, EXCHANGE1, KEY1)
    channel.queue_bind(QUEUE2, EXCHANGE2, KEY2)
    channel.exchange_bind(EXCHANGE2, EXCHANGE1, KEY2)

    channel.basic_publish(EXCHANGE1, KEY1, 'message 1')
    channel.basic_publish(EXCHANGE1, KEY2, 'message 2')

    show_message(channel, QUEUE1, *channel.basic_get(QUEUE1))
    show_message(channel, QUEUE1, *channel.basic_get(QUEUE1))
    show_message(channel, QUEUE2, *channel.basic_get(QUEUE2))
    show_message(channel, QUEUE2, *channel.basic_get(QUEUE2))

    channel.queue_delete(QUEUE1)
    channel.queue_delete(QUEUE2)
    channel.exchange_delete(EXCHANGE1)
    channel.exchange_delete(EXCHANGE2)

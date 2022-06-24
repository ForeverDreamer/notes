from pika.exchange_type import ExchangeType

from utilts import *


EXCHANGE = 'ex.topic'
QUEUE1 = 'queue1'
QUEUE2 = 'queue2'
QUEUE3 = 'queue3'

with get_channel() as channel:
    channel.exchange_declare(EXCHANGE, ExchangeType.topic)
    channel.queue_declare(QUEUE1)
    channel.queue_declare(QUEUE2)
    channel.queue_declare(QUEUE3)
    channel.queue_bind(QUEUE1, EXCHANGE, '*.image.*')
    channel.queue_bind(QUEUE2, EXCHANGE, '#.image')
    channel.queue_bind(QUEUE3, EXCHANGE, 'image.#')

    channel.basic_publish(EXCHANGE, 'convert.image.bmp', 'convert.image.bmp'.encode('utf-8'))
    channel.basic_publish(EXCHANGE, 'convert.bitmap.image', 'convert.bitmap.image'.encode('utf-8'))
    channel.basic_publish(EXCHANGE, 'image.bitmap.32bit', 'convert.bitmap.32bit'.encode('utf-8'))

    show_message(channel, QUEUE1, *channel.basic_get(QUEUE1))
    show_message(channel, QUEUE2, *channel.basic_get(QUEUE2))
    show_message(channel, QUEUE3, *channel.basic_get(QUEUE3))

    channel.queue_delete(QUEUE1)
    channel.queue_delete(QUEUE2)
    channel.queue_delete(QUEUE3)
    channel.exchange_delete(EXCHANGE)


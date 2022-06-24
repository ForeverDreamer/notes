from pika.exchange_type import ExchangeType

from utilts import *

EXCHANGE = 'ex.headers'
QUEUE1 = 'queue1'
QUEUE2 = 'queue2'

with get_channel() as channel:
    channel.exchange_declare(EXCHANGE, ExchangeType.headers)
    channel.queue_declare(QUEUE1)
    channel.queue_declare(QUEUE2)
    channel.queue_bind(QUEUE1, EXCHANGE, arguments={'x-match': 'all', 'job': 'convert', 'format': 'jpeg'})
    channel.queue_bind(QUEUE2, EXCHANGE, arguments={'x-match': 'any', 'job': 'convert', 'format': 'jpeg'})

    channel.basic_publish(EXCHANGE, '', 'message 1'.encode('utf-8'),
                          pika.BasicProperties(headers={'job': 'convert', 'format': 'jpeg'}))
    channel.basic_publish(EXCHANGE, '', 'message 2'.encode('utf-8'),
                          pika.BasicProperties(headers={'job': 'convert', 'format': 'bmp'}))

    show_message(channel, QUEUE1, *channel.basic_get(QUEUE1))
    show_message(channel, QUEUE1, *channel.basic_get(QUEUE1))
    print('---------------------------------------')
    show_message(channel, QUEUE2, *channel.basic_get(QUEUE2))
    show_message(channel, QUEUE2, *channel.basic_get(QUEUE2))

    channel.queue_delete(QUEUE1)
    channel.queue_delete(QUEUE2)
    channel.exchange_delete(EXCHANGE)

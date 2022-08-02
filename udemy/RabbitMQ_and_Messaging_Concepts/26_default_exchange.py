from utils import *


QUEUE1 = 'queue1'
QUEUE2 = 'queue2'

with get_channel() as channel:
    channel.queue_declare(QUEUE1)
    channel.queue_declare(QUEUE2)

    channel.basic_publish('', QUEUE1, 'message 1'.encode('utf-8'))
    channel.basic_publish('', QUEUE2, 'message 2'.encode('utf-8'))

    show_message(channel, QUEUE1, *channel.basic_get(QUEUE1))
    show_message(channel, QUEUE1, *channel.basic_get(QUEUE1))
    show_message(channel, QUEUE2, *channel.basic_get(QUEUE2))
    show_message(channel, QUEUE2, *channel.basic_get(QUEUE2))

    channel.queue_delete(QUEUE1)
    channel.queue_delete(QUEUE2)

from pika.exchange_type import ExchangeType

from utilts import *

EX_FANOUT = 'ex.fanout'
EX_DIRECT = 'ex.direct'
QUEUE1 = 'queue1'
QUEUE2 = 'queue2'
QUEUE_DISCARDED = 'queue_discarded'
KEY_VIDEO = 'key_video'
KEY_IMAGE = 'key_image'
KEY_TEXT = 'key_text'


with get_channel() as channel:
    channel.exchange_declare(EX_FANOUT, ExchangeType.fanout)
    channel.exchange_declare(EX_DIRECT, ExchangeType.direct, arguments={'alternate-exchange': EX_FANOUT})
    channel.queue_declare(QUEUE1)
    channel.queue_declare(QUEUE2)
    channel.queue_declare(QUEUE_DISCARDED)

    channel.queue_bind(QUEUE1, EX_DIRECT, KEY_VIDEO)
    channel.queue_bind(QUEUE2, EX_DIRECT, KEY_IMAGE)
    channel.queue_bind(QUEUE_DISCARDED, EX_FANOUT, '')

    channel.basic_publish(EX_DIRECT, KEY_VIDEO, 'message video'.encode('utf-8'))
    channel.basic_publish(EX_DIRECT, KEY_TEXT, 'message text'.encode('utf-8'))

    show_message(channel, QUEUE1, *channel.basic_get(QUEUE1))
    show_message(channel, QUEUE2, *channel.basic_get(QUEUE2))
    show_message(channel, QUEUE_DISCARDED, *channel.basic_get(QUEUE_DISCARDED))

    channel.queue_delete(QUEUE1)
    channel.queue_delete(QUEUE2)
    channel.queue_delete(QUEUE_DISCARDED)
    channel.exchange_delete(EX_FANOUT)
    channel.exchange_delete(EX_DIRECT)

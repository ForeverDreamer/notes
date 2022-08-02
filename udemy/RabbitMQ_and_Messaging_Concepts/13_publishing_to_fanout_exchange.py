from pika.exchange_type import ExchangeType

from utils import get_channel

with get_channel() as channel:
    channel.exchange_declare('ex.fanout', ExchangeType.fanout)
    channel.queue_declare('my.queque1')
    channel.queue_declare('my.queque2')
    channel.queue_bind('my.queque1', 'ex.fanout', '')
    channel.queue_bind('my.queque2', 'ex.fanout', '')

    channel.basic_publish('ex.fanout', '', 'Message 1')
    channel.basic_publish('ex.fanout', '', 'Message 2')
    input('按任意键退出：')
    channel.queue_delete('my.queque1')
    channel.queue_delete('my.queque2')
    channel.exchange_delete('ex.fanout')


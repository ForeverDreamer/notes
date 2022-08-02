from utils import *


def on_message_queque1(_channel, method, properties, body):
    print('---------------------on_message_queque1---------------------')
    print(method.delivery_tag)
    print(properties)
    print(body.decode('utf-8'))
    print()
    _channel.basic_ack(delivery_tag=method.delivery_tag)


def on_message_queque2(_channel, method, properties, body):
    print('---------------------on_message_queque2---------------------')
    print(method.delivery_tag)
    print(properties)
    print(body.decode('utf-8'))
    print()
    _channel.basic_ack(delivery_tag=method.delivery_tag)


with get_channel() as channel:
    channel.basic_consume('my.queque1', on_message_queque1)
    channel.basic_consume('my.queque2', on_message_queque2)
    try:
        print('start_consuming')
        channel.start_consuming()
    except KeyboardInterrupt:
        print('stop_consuming')
        channel.stop_consuming()

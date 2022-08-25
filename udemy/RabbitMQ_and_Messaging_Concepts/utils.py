import contextlib
import sys

import pika


@contextlib.contextmanager
def get_channel():
    # <ENTER>
    # Set the connection parameters to connect to rabbit-server1 on port 5672
    # on the / virtual host using the username "guest" and password "guest"
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost',
                                           5672,
                                           '/',
                                           credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    print('连接开启！')
    try:
        # Like __enter__()'s return statement
        yield channel
        # <NORMAL EXIT>
        channel.close()
        connection.close()
        print('连接关闭！')
    except Exception:
        # <EXCEPTIONAL EXIT>
        print('pika channel: exceptional exit', sys.exc_info())
        raise


def show_message(channel, queue, method, properties, body):
    print('队列: ', queue)
    if method:
        print(method, properties, body.decode('utf-8'))
        channel.basic_ack(method.delivery_tag)
    else:
        print('No message returned')


def exchange_clear(channel):
    channel.exchange_delete('ex.direct')


def queue_clear(channel):
    # channel.queue_delete('queue1')
    # channel.queue_delete('queue2')
    channel.queue_delete('queue.infos')
    channel.queue_delete('queue.warnings')
    channel.queue_delete('queue.errors')

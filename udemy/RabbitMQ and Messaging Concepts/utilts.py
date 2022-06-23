import contextlib

import pika


@contextlib.contextmanager
def get_channel():
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
    yield channel
    channel.close()
    connection.close()
    print('连接关闭！')




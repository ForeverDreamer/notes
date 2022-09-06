import sys
sys.path.append(r"D:\data_files\notes\udemy\RabbitMQ_and_Messaging_Concepts")

from utils import get_channel

EXCHANGE = 'logs'


# shell 1
# python emit_log.py
with get_channel() as channel:
    channel.exchange_declare(exchange=EXCHANGE, exchange_type='fanout')
    message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    channel.basic_publish(exchange=EXCHANGE, routing_key='', body=message)
    print(" [x] Sent %r" % message)

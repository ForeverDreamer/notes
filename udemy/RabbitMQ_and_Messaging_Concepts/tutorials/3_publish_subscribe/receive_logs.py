import sys
sys.path.append(r"D:\data_files\notes\udemy\RabbitMQ_and_Messaging_Concepts")
import time

from utils import get_channel


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


# shell 2
# python receive_logs.py
# shell 3
# python receive_logs.py
try:
    with get_channel() as channel:
        channel.exchange_declare(exchange='logs', exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange='logs', queue=queue_name)
        print(' [*] Waiting for logs. To exit press CTRL+C')
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
except KeyboardInterrupt:
    print('Interrupted')
    channel.stop_consuming()

import sys
sys.path.append(r"D:\data_files\notes\udemy\RabbitMQ_and_Messaging_Concepts")
import time

from utils import get_channel

QUEUE = 'task_queue'


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# shell 1
# python worker.py

# shell 2
# python worker.py
try:
    with get_channel() as channel:
        channel.queue_declare(queue=QUEUE, durable=True)
        channel.basic_consume(
            queue=QUEUE,
            on_message_callback=callback,
        )
        channel.basic_qos(prefetch_count=1)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
except KeyboardInterrupt:
    print('Interrupted')
    channel.stop_consuming()

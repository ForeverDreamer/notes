import sys
sys.path.append(r"D:\data_files\notes\udemy\RabbitMQ_and_Messaging_Concepts")

import pika

from utils import get_channel

QUEUE = 'task_queue'


# shell 3
# python new_task.py One sec.
# python new_task.py Two secs..
# python new_task.py Three secs...
# python new_task.py Four secs....
# python new_task.py Ten secs..........
# python new_task.py Twenty secs....................
with get_channel() as channel:
    channel.queue_declare(queue=QUEUE, durable=True)
    message = ' '.join(sys.argv[1:]) or "Hello World!"
    channel.basic_publish(
        exchange='',
        routing_key=QUEUE,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        )
    )
    print(" [x] Sent %r" % message)

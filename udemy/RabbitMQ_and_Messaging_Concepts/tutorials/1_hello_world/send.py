from utils import get_channel


QUEUE = 'hello'

with get_channel() as channel:
    channel.queue_declare(queue=QUEUE)
    channel.basic_publish(exchange='',
                          routing_key=QUEUE,
                          body='Hello World!')
    print(" [x] Sent 'Hello World!'")

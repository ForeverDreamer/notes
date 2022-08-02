from utils import get_channel

QUEUE = 'hello'


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


if __name__ == '__main__':
    try:
        with get_channel() as channel:
            channel.queue_declare(queue=QUEUE)
            channel.basic_consume(
                queue=QUEUE,
                on_message_callback=callback,
                auto_ack=True,
            )
            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()
    except KeyboardInterrupt:
        print('Interrupted')
        channel.stop_consuming()

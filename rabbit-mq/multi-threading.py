from threading import Thread
import pika


class Producer(Thread):
    def run(self) -> None:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='logs', exchange_type='fanout')

        while True: # blocks
            message = input()
            channel.basic_publish(exchange='logs', routing_key='',
                                  body="Teacher: {}".format(message))
        print("User input finished")

        connection.close()


class Consumer(Thread):
    def run(self) -> None:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost'))

        channel = connection.channel()

        channel.exchange_declare(exchange='logs', exchange_type='fanout')

        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange='logs', queue=queue_name)

        def callback(ch, method, propertires, body):
            print(" [x]: {}".format(body))

        channel.basic_consume(queue=queue_name, on_message_callback=callback,
                              auto_ack=True)

        channel.start_consuming() # blocks
        print("consumer finished")

# Main Thread
producer = Producer()   # create a producer on separate thread
producer.start()
print("producer created")
consumer = Consumer()   # create a consumer on separate thread
consumer.start()
print("consumer created")

# end of Main Thread









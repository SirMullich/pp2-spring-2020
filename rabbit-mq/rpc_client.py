from threading import Thread
import pika
import uuid


class RpcConsumer(Thread):
    def __init__(self, binding_key):
        Thread.__init__(self)
        self.binding_key = binding_key
        self.cb = None  # callback function
        self.corr_id = None
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()
        self.channel.queue_declare(self.binding_key, exclusive=True)
        self.channel.queue_bind(exchange='X:routing.topic',
                                queue=self.binding_key, routing_key=self.binding_key)

    def run(self):
        def callback(ch, method, props, body):
            if self.corr_id == props.correlation_id:
                self.response = body
                decoded = body.decode('utf-8') # decoded string

                if self.cb is not None:
                    self.cb(decoded)
            else:
                print("Unexpected response: {}".format(body))

        self.channel.basic_consume(queue=self.binding_key, on_message_callback=callback, auto_ack=True)
        print("Starting RPC consumer")
        self.connection.process_data_events()
        self.channel.start_consuming() # blocks thread

    def set_callback(self, corr_id, cb):
        self.corr_id = corr_id
        self.cb = cb


class RpcClient(Thread):
    def __init__(self, queue_name, rpc_consumer):
        Thread.__init__(self)
        self.rpc_consumer = rpc_consumer
        self.queue_name = queue_name
        self.exchange = 'X:routing.topic'
        self.corr_id = None
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

    def run(self) -> None:
        pass

    def call(self, request, rk, cb):
        self.corr_id = str(uuid.uuid4())
        self.rpc_consumer.set_callback(self.corr_id, cb)

        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=rk,
            properties=pika.BasicProperties(
                reply_to=self.queue_name,
                correlation_id=self.corr_id
            ),
            body=str(request)
        )
        print("publishing: {}, replyTo: {}, corr_id: {}".format(str(request), self.queue_name, self.corr_id))



def handle_square_response(num):
    print('Received square response: {}'.format(num))

def handle_fib_response(num):
    print('Received fib response: {}'.format(num))

def handle_sum_response(num):
    print('Received sum response: {}'.format(num))


queue_name = "{}.response".format(uuid.uuid4())
rpc_consumer = RpcConsumer(queue_name)
rpc_consumer.daemon = True
rpc_consumer.start()

rpc_client = RpcClient(queue_name, rpc_consumer)
rpc_client.daemon = True
rpc_client.start()

while True:
    message = input()
    params = message.split()
    if params[0] == 'square':
        rpc_client.call(params[1], 'request.square', handle_square_response)
    elif params[0] == 'fib':
        rpc_client.call(params[1], 'request.fib', handle_fib_response)
    elif params[0] == 'sum':
        rpc_client.call(params[1], 'request.sum', handle_sum_response)
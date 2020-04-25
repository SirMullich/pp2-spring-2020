import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.exchange_declare(exchange='X:routing.topic', exchange_type='topic', durable=True)

channel.queue_declare(queue='rpc_queue')

binding_keys = ['request.square', 'request.fib', 'request.sum']

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='X:routing.topic',
        queue='rpc_queue',
        routing_key=binding_key
    )

def square(n):
    return n * n

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def sum(n): # 1 + 2 + 3 + 4 + ... + n = n * (n + 1) / 2
    return n * (n + 1) // 2

def on_request(ch, method, props, body):
    n = int(body)
    response = 1
    if method.routing_key == 'request.square':
        response = square(n)
        print(" [.] square(%s)" % n)
    elif method.routing_key == 'request.fib':
        response = fib(n)
        print(" [.] fib(%s)" % n)
    elif method.routing_key == 'request.sum':
        response = sum(n)
        print(" [.] sum(%s)" % n)

    ch.basic_publish(exchange='X:routing.topic',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
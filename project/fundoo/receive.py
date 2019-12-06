import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='X')
channel.queue_bind(exchange='X', queue='hello', routing_key='#')

channel.basic_publish(exchange='X',
    routing_key='sachinsanju04@gmail.com',
    properties=pika.BasicProperties(
        content_type = 'text/plain',
        headers = {'Subject':'Greetings'}),
    body='Hello world!')
connection.close()

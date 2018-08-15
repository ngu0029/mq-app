# -*- coding: utf-8 -*-

import requests
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode("utf-8"))
    
    # post the text message to the web page
    # change to 172.17.0.4:5000 in case you use this ip addr of the http server's container assigned on your local host
    # change to 127.0.0.1:5000 in case you run with local Anaconda IPython
	# Use --link for networking between containers
    requests.post("http://server-app:5000", data={'text': body.decode("utf-8")})

def rabbitMsgQueue():
    # establish a connection with localhost message broker server
    # change to 172.17.0.2:5672 in case you use this ip addr of the rabbitmq's container assigned on your local host
    # change to 127.0.0.1:80 in case you run with local Anaconda IPython
	# Use --link for networking between containers
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='my-rabbitmq',\
                                                                   port=5672))
    channel = connection.channel()
    
    channel.queue_declare(queue='rabbitQueue')
    
    # callback function to receive message from the message queue
    channel.basic_consume(callback,
                          queue='rabbitQueue',
                          no_ack=True)
    
    # never-ending loop that waits for data and runs callbacks
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

rabbitMsgQueue()


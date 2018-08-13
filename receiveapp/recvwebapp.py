# -*- coding: utf-8 -*-

import requests
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode("utf-8"))
    
    # post the text message to the web page
    # 172.17.0.4 is the http server's container ip address
    # change to 127.0.0.1:5000 in case you run with local anaconda IPython
    requests.post("http://172.17.0.4:5000", data={'text': body.decode("utf-8")})

def rabbitMsgQueue():
    # establish a connection with localhost message broker server
    # 172.17.0.2 is the rabbitmq's container ip address
    # change to 127.0.0.1:80 in case you run with local anaconda IPython
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.2',\
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


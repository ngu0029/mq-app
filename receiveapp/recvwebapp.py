# -*- coding: utf-8 -*-

import requests
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode("utf-8"))
    
    # post the text message to the web page
    requests.post("http://127.0.0.1:5000", data={'text': body.decode("utf-8")})

def rabbitMsgQueue():
    # establish a connection with localhost message broker server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',\
                                                                   port=80))
    channel = connection.channel()
    
    channel.queue_declare(queue='rabbitQueue')
    
    # callback function to receive message from the message queue
    channel.basic_consume(callback,
                          queue='rabbitQueue',
                          no_ack=True)
    
    # never-ending loop that waits for data and runs callbacks
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

rabbitMsgQueue()# -*- coding: utf-8 -*-


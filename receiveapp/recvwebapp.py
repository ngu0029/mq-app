# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify
 
app = Flask(__name__)

msg = 'Hello!'

@app.route('/text')
def printText(msg):
    return msg

#if __name__ == '__main__':
#    app.run(port=5000, host='127.0.0.1')

import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode("utf-8"))
    
    printText(body.decode("utf-8"))


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

rabbitMsgQueue()
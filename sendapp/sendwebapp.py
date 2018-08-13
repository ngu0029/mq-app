# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO
import pika

def rabbitMsgQueue(message):
    # establish a connection with localhost message broker server
    # 172.17.0.2 is the rabbitmq's container ip address
    # change to 127.0.0.1:80 in case you run with local anaconda IPython
    connection = pika.BlockingConnection(pika.ConnectionParameters('172.17.0.2',\
                                                                   port=5672))
    channel = connection.channel()
    
    # create the text queue to which the message will be delivered
    channel.queue_declare(queue='rabbitQueue')
    
    # Send the message to the message queue
    channel.basic_publish(exchange='',\
                          routing_key='rabbitQueue',\
                          body=message)
    print(' [x] Sent %r' %message)
    
    # close the connection
    connection.close()

# listen on standard https port and receive only one post parameter namely text
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        
        # deliver the message to message queue
        message = str(body).split('=')[1][:-1] # remove single quote at the end
        #print(message)
        rabbitMsgQueue(message)
        
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
        
httpd = HTTPServer(('127.0.0.1', 443), SimpleHTTPRequestHandler)
httpd.serve_forever()

# Using command prompt -- DO POST
# try: curl -k --data "text=for-bar" http://localhost:443/
# output: This is POST request. Received: text=for-bar

# Using a browser like Chrome -- DO GET
# try: http://localhost:443/
# display: Hello, world!

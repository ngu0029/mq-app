# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO

class initialText:
    def show(self):
        return "Initial Text".encode('utf-8')

class http_server:
    def __init__(self, text):
        # change to 172.17.0.4:5000 in case you use this ip addr of the http server's container assigned on your local host
        # change to 127.0.0.1:5000 in case you run with local Anaconda IPython
        server = HTTPServer(('0.0.0.0', 5000), SimpleHTTPRequestHandler)
        server.text = text
        server.serve_forever()

# listen on standard http port 5000 and receive only one post parameter namely text
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
       
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(self.server.text)
        self.wfile.write(response.getvalue())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        
        # store the text message
        msg = str(body).split('=')[1][:-1] # remove single quote at the end
        self.server.text = msg.encode('utf-8')
        print(self.server.text)
        
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

class main:
    def __init__(self):
        text = initialText()
        self.text = text.show()
        self.server = http_server(self.text)

if __name__ == '__main__':
    m = main()

# Using command prompt -- DO POST
# try: curl -k --data "text=for-bar" http://localhost:5000/
# output: This is POST request. Received: text=for-bar

# Using a browser like Chrome -- DO GET
# try: http://localhost:5000/
# display: Hello, world!

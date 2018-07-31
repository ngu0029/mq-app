============= SETUP =============
1. Running the daemon of RabbitMQ Docker image
- Open a Windows PowerShell
- Run the daemon of RabbitMQ Docker
PS C:\Users\T901> docker run -d --hostname my-rabbit --name my-rabbitmq -p 80:5672 rabbitmq:3

Here I map the container’s port 5672 to the localhost’s port 80. You can specify the public ip address 
and port of the RabbitMQ server.
e.g. docker run -d --hostname my-rabbit --name my-rabbitmq -p rabbitmqip:port:5672 rabbitmq:3

2. Build and run Python Docker image for the sending app
- Open a new Windows PowerShell
- Go to the directory of the sending app; then enter the following commands to build and run 
Python Docker image for the sending app
a. PS D:\github\mq-app\sendapp> docker build -t my-sending-app .
b. PS D:\github\mq-app\sendapp> docker run -it --rm --name send-app -p 443:443 -p 80:80 my-sending-app

Here I map the container’s port 80 to the localhost’s port 80. You can specify the public ip address 
and port of the RabbitMQ server.
e.g. docker run -it --rm --name send-app -p 443:443 -p rabbitmqip:port:80 my-sending-app

3. Build and run Python Docker image for the receiving app
- Open a new Windows PowerShell
- Go to the directory of the receiving app; then enter the following commands to build and run Python Docker image for the receiving app
a. PS D:\github\mq-app\receiveapp> docker build -t my-receiving-app .
b. PS D:\github\mq-app\receiveapp> docker run -it --rm --name receive-app -p 443:443 -p 80:80 my-receiving-app

Here I map the container’s port 80 to the localhost’s port 80. You can specify the public ip address and 
port of the RabbitMQ server.
e.g. docker run -it --rm --name receive-app -p 443:443 -p rabbitmqip:port:80 my-receiving-app


============= TEST =============
1. Open a command prompt (CMD), and enter curl command to do HTTP Post
curl -k --data "text=HELLO" http://127.0.0.1:443/
2. Open web browser, e.g. Chrome, and browser to the localhost at port 5000 http://127.0.0.1:5000/text
You would see the text, for example: HELLO, on the web page.
3. Change the text parameter in the curl command to see the change in the content of the web page





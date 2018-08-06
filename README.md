Prerequisites:
- Install Docker on Windows (https://docs.docker.com/docker-for-windows/)
- Install Anaconda for Python 3.6 on Windows (https://www.anaconda.com/download/). This installation is only for 
the setup 2 option in case you want to run Python applications with IPython on your local PC.

Note: I have set up and tested the applications on Windows 10 Pro laptop.

You can choose Setup 1 option or Setup 2 option depending on the fact that you want to run Python application 
with Docker or IPython.

============= SETUP 1 OPTION =============
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

3. Build and run Python Docker image for the http server app to receive the text message post
- Open a new Windows PowerShell
- Go to the directory of the server app; then enter the following commands to build and 
run Python Docker image for the server app
a. PS D:\github\mq-app\server> docker build -t my-server-app .
b. PS D:\github\mq-app\server> docker run -it --rm --name server-app -p 5000:5000 my-server-app
Here I map the container’s port 5000 to the localhost’s port 5000. The web server is running on local host.

4. Build and run Python Docker image for the receiving app
- Open a new Windows PowerShell
- Go to the directory of the receiving app; then enter the following commands to build and run 
Python Docker image for the receiving app
a. PS D:\github\mq-app\receiveapp> docker build -t my-receiving-app .
b. PS D:\github\mq-app\receiveapp> docker run -it --rm --name receive-app -p 5000:5000 -p 80:80 my-receiving-app

Here I map the container’s port 80 to the localhost’s port 80. You can specify the public ip address and 
port of the RabbitMQ server.
e.g. docker run -it --rm --name receive-app -p 5000:5000 -p rabbitmqip:port:80 my-receiving-app


============= SETUP 2 OPTION =============
1. Running the daemon of RabbitMQ Docker image
- Open a Windows PowerShell
- Run the daemon of RabbitMQ Docker
PS C:\Users\T901> docker run -d --hostname my-rabbit --name my-rabbitmq -p 80:5672 rabbitmq:3

Here I map the container’s port 5672 to the localhost’s port 80. You can specify the public ip address 
and port of the RabbitMQ server.
e.g. docker run -d --hostname my-rabbit --name my-rabbitmq -p rabbitmqip:port:5672 rabbitmq:3

2. Running the sending web application
- Open a new Windows PowerShell
- Go to Anaconda IPython script directory and run the sending web app
PS C:\Users\T901\Anaconda3\Scripts> .\ipython D:\github\mq-app\sendapp\sendwebapp.py

3. Running the http server application to receive the text message post
- Open a new Windows PowerShell
- Go to Anaconda IPython script directory and run the http server application
PS C:\Users\T901\Anaconda3\Scripts> .\ipython D:\github\mq-app\server\httpserver.py

4. Running the receiving web application
- Open a new Windows PowerShell
- Go to Anaconda IPython script directory and run the receiving web app
PS C:\Users\T901\Anaconda3\Scripts> .\ipython D:\github\mq-app\receiveapp\recvwebapp.py



============= TEST =============
1. Open a command prompt (CMD), and enter curl command to do HTTP Post
curl -k --data "text=HELLO" http://127.0.0.1:443/
2. Open web browser, e.g. Chrome, and browser to the localhost at port 5000 http://127.0.0.1:5000
You would see the text, for example: HELLO, on the web page.
3. Change the text parameter in the curl command, then repeat the curl command on the command prompt and 
check the web page is updated with the new message






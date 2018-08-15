Prerequisites:
- Install Docker on Windows (https://docs.docker.com/docker-for-windows/)
- Install Anaconda for Python 3.6 on Windows (https://www.anaconda.com/download/). This installation is only for 
the setup 3 option in case you want to run Python applications with IPython on your local PC.

Note: I have set up and tested the applications on Windows 10 Pro laptop. 
Using Docker for Windows on Windows 10 Pro, you must also switch to Linux containers.

You can choose:
- Setup 1 option if you want to do the setup in one shot with the bash script
- Setup 2 option if you want to do the setup by running each application in different PowerShells
to see the output on each application when you do the test
- Setup 3 option if you want to run Python applications with local Anaconda IPython

Finally, do the test.


============= SETUP 1 OPTION =============
- Open a Windows PowerShell
- Go to your application directory (where you store the directories and files of your 
message queue project) and run the running_services.sh script

e.g. PS D:\github\mq-app> .\running_services.sh


============= SETUP 2 OPTION =============
1. Running the daemon of RabbitMQ Docker image
- Open a Windows PowerShell
- Run the daemon of RabbitMQ Docker

PS C:\Users\T901> docker run -d --hostname my-rabbit --name my-rabbitmq -p 80:5672 rabbitmq:3

Here I map the container’s port 5672 to the localhost’s port 80. You can specify the public ip address 
and port of the RabbitMQ server in case of use.

e.g. docker run -d --hostname my-rabbit --name my-rabbitmq -p rabbitmqip:port:5672 rabbitmq:3

2. Build and run Python Docker image for the sending app
- Open a new Windows PowerShell
- Go to the directory of the sending app; then enter the following commands to build and run 
Python Docker image for the sending app

a. PS D:\github\mq-app\sendapp> docker build -t my-sending-app .

b. PS D:\github\mq-app\sendapp> docker run -it --rm --name send-app -p 443:443 --link my-rabbitmq:my-rabbitmq my-sending-app

Here:
I map the container’s port 443 to the localhost’s port 443. You can execute the curl command to http://127.0.0.1:443.
I use --link to connect the sending app container to the rabbitmq service.
You can specify the public ip address and port of the RabbitMQ server in case of use.

3. Build and run Python Docker image for the http server app to receive the text message post
- Open a new Windows PowerShell
- Go to the directory of the server app; then enter the following commands to build and 
run Python Docker image for the server app

a. PS D:\github\mq-app\server> docker build -t my-server-app .

b. PS D:\github\mq-app\server> docker run -it --rm --name server-app -p 5000:5000 my-server-app

Here I map the container’s port 5000 to the localhost’s port 5000. You can access the web page via http://127.0.0.1:5000.

4. Build and run Python Docker image for the receiving app
- Open a new Windows PowerShell
- Go to the directory of the receiving app; then enter the following commands to build and run 
Python Docker image for the receiving app

a. PS D:\github\mq-app\receiveapp> docker build -t my-receiving-app .

b. PS D:\github\mq-app\receiveapp> docker run -it --rm --name receive-app -p 8080:8080 --link my-rabbitmq:my-rabbitmq --link server-app:server-app my-receiving-app

Here I use --link to connect the sending app container to the rabbitmq and http server services.
You can specify the public ip address and port of the RabbitMQ server in case of use.


============= SETUP 3 OPTION =============
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
1. Open a command prompt window (CMD), and execute curl command to do HTTP Post to 
the localhost at port 443 http://127.0.0.1:443/

C:\Users\T901>curl -k --data "text=HELLO" http://127.0.0.1:443/

2. Open web browser, e.g. Chrome, and browser to the localhost at port 5000 http://127.0.0.1:5000
You would see the text, for example: HELLO, on the web page.

3. Change the text parameter in the curl command, then repeat the curl command on the command prompt and 
check the web page is updated with the new message

#!/bin/bash

clear

echo "The running script starts now"
echo

echo "Running the daemon of RabbitMQ Docker image"
echo "docker run -d --hostname my-rabbit --name my-rabbitmq -p 80:5672 rabbitmq:3"
#detach the container with -d (run in the background)
docker run -d --hostname my-rabbit --name my-rabbitmq -p 80:5672 rabbitmq:3
echo

echo "Build and run Python Docker image for the sending app"
echo "docker build -t my-sending-app ."
echo "docker run -d -it --rm --name send-app -p 443:443 my-sending-app"
cd sendapp
docker build -t my-sending-app .
#detach the container with -d (run in the background)
docker run -d -it --rm --name send-app -p 443:443 --link my-rabbitmq:my-rabbitmq my-sending-app
echo

echo "Build and run Python Docker image for the http server app"
echo "docker build -t my-server-app ."
echo "docker run -d -it --rm --name server-app -p 5000:5000 my-server-app"
cd ..
cd server
docker build -t my-server-app .
#detach the container with -d (run in the background)
docker run -d -it --rm --name server-app -p 5000:5000 my-server-app
#run a single Python script
#docker run -d -it --rm --name server-app -p 5000:5000 -v D:/github/mq-app/server:/server -w /server python:3 python httpserver.py
echo

echo "Build and run Python Docker image for the receiving app"
echo "docker build -t my-receiving-app ."
echo "docker run -d -it --rm --name receive-app -p 8080:8080 my-receiving-app"
cd ..
cd receiveapp
sleep 10s
docker build -t my-receiving-app .
#detach the container with -d (run in the background)
docker run -d -it --rm --name receive-app -p 8080:8080 --link my-rabbitmq:my-rabbitmq --link server-app:server-app my-receiving-app
echo

cd ..
docker ps -a
echo "The script finishes"

$SHELL
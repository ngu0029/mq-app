#!/bin/bash

clear

echo "The removing script starts now"
echo

docker ps -a
echo

echo "docker stop my-rabbitmq send-app server-app receive-app"
docker stop my-rabbitmq send-app server-app receive-app
echo

echo "docker rm my-rabbitmq send-app server-app receive-app"
docker rm my-rabbitmq send-app server-app receive-app
echo

docker ps -a
echo

echo "The script finishes"

$SHELL
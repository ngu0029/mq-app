#!/bin/bash

clear

echo "The running script starts now"
echo

echo "Create and start the services"
echo "docker-compose up"
docker-compose up
echo

docker-compose ps
echo "The script finishes"

$SHELL
#!/bin/bash

clear

echo "The removing script starts now"
echo

docker-compose ps
echo

echo "docker-compose down"
docker-compose down
echo

docker-compose ps
echo

echo "The script finishes"

$SHELL
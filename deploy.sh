#!/bin/bash

docker build -t animal_noises_server server

docker build -t animal_api animal_api

docker network create animal_noises_network

docker run -d -p 5000:5000 --name animal_server --network animal_noises_network animal_noises_server
docker run -d --name animal_api --network animal_noises_network animal_api
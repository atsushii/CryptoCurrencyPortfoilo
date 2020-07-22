#!/bin/bash

echo "***********************************"
echo "**** Building Docker test image ***"
echo "***********************************"

docker-compose -f ../docker-compose.test.yml build


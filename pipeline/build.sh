#!/bin/bash

echo "***********************************"
echo "**** Building Docker test image ***"
echo "***********************************"
#tesr
docker-compose -f ../docker-compose.test.yml build


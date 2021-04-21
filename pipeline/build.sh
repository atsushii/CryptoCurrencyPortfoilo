#!/usr/bin/bash

echo "***********************************"
echo "**** Building Docker test image ***"
echo "***********************************"
#tes4
docker build -f ../api/Dockerfile.test -t dockertest .



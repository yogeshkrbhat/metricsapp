#!/bin/bash
app="metricsapp"
docker build -t ${app} .
docker rm -f  ${app}
docker run  -d   -p 56733:80 -p 56734:8000   --name=${app}   -v $PWD:/app  ${app}

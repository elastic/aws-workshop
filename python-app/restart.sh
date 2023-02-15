#!/bin/bash

sudo pkill -f app1.py
sudo pkill -f loadgen.py
sudo python3 /home/ubuntu/aws-workshop/python-app/app1.py &
sleep 1
sudo python3 /home/ubuntu/aws-workshop/python-app/loadgen.py &
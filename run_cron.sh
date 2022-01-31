#!/bin/bash  
cd /home/vid/PHP/lotoes-server
source bin/activate
# you should specifiy the python version in the below command
#python2.7 start.py >> /Users/X/Code/python/example/log.txt 2>&1
python3 cron.py >> /home/vid/PHP/lotoes-server/log.txt 2>&1

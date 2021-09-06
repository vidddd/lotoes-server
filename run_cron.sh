#!/bin/bash  
#or whatever shell you use
cd /home/vid/PHP/lotoes-server
.  /home/vid/.local/share/virtualenvs/lotoes-server-e9LUELRz/bin/activate
# you should specifiy the python version in the below command
#python2.7 start.py >> /Users/X/Code/python/example/log.txt 2>&1
python3 cron.py >> /home/vid/PHP/lotoes-server/log.txt 2>&1

#!/bin/bash

core-daemon > /var/log/core-daemon.log &
sleep 1

core-gui &

# connect to maci-backend or open a shell
wget $BACKEND:63658/workers/script.py -O /worker/worker.py \
    || bash

python -u /worker/worker.py --backend $BACKEND:63658 --capabilities core --maxidletime $IDLE --no-clear-tmp-dir 


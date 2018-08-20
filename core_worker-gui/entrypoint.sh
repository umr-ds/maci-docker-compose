#!/bin/bash

core-daemon > /var/log/core-daemon.log 2>&1 &
sleep 1

core-gui > /var/log/core-gui.log 2>&1 &

# connect to maci-backend or open a shell
wget $BACKEND:63658/workers/script.py -O /worker/worker.py &&
    python -u /worker/worker.py --backend $BACKEND:63658 --capabilities core --maxidletime $IDLE --no-clear-tmp-dir &&
    exit
    
echo "Couldn't connect to MACI backend, falling back to bash..." && bash

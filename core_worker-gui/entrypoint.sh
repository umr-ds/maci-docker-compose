#!/bin/bash

core-daemon > /var/log/core-daemon.log 2>&1 &
sleep 1

core-gui $CORE_PARAMS > /var/log/core-gui.log 2>&1 &
CORE_GUI_PID=$!

# connect to maci-backend or open a shell
wget $BACKEND:63658/workers/script.py -O /worker/worker.py &&
    python -u /worker/worker.py --backend $BACKEND:63658 --capabilities core --maxidletime $IDLE --no-clear-tmp-dir &&
    exit
    
echo "Couldn't connect to MACI backend, waiting until core-gui is closed..." && wait $CORE_GUI_PID

#!/bin/bash

core-daemon > /var/log/core-daemon.log &

wget $BACKEND:63658/workers/script.py -O /worker/worker.py
python -u /worker/worker.py --backend $BACKEND:63658 --capabilities core --maxidletime $IDLE --no-clear-tmp-dir 


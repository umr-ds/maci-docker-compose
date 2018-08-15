#!/bin/bash
export GEOMETRY=${SCREEN_WIDTH}x${SCREEN_HEIGHT}x${SCREEN_DEPTH}
x11vnc -storepasswd ${PASSWORD} ~/.vnc/passwd

sleep 10

wget $BACKEND:63658/workers/script.py -O /worker/worker.py
python -u /worker/worker.py --backend $BACKEND:63658 --capabilities core --maxidletime $IDLE --no-clear-tmp-dir &

exec /usr/bin/supervisord -n


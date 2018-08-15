#!/bin/bash
export GEOMETRY=${SCREEN_WIDTH}x${SCREEN_HEIGHT}x${SCREEN_DEPTH}
x11vnc -storepasswd ${PASSWORD} ~/.vnc/passwd

sleep 10

python -u /worker/worker.py --backend maci-backend:63658 --maxidletime -1 --capabilities core --no-clear-tmp-dir &

exec /usr/bin/supervisord -n


#!/bin/bash

echo "# Starting SSHD"
/usr/sbin/sshd -D &

if [ ! -z "$BACKEND" ]; then
    echo "# Starting MACI worker (BACKEND=$BACKEND)"
    wget $BACKEND:63658/workers/script.py -O /worker/worker.py &&
        python -u /worker/worker.py --backend $BACKEND:63658 --capabilities $CAP --maxidletime $IDLE --no-clear-tmp-dir &&
        exit

    echo "# Couldn't connect to MACI backend." &&
        exit 1
else
    echo "# Dropping into bash (exit with ^D or \`exit\`)"
    bash
fi

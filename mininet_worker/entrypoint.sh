#!/bin/bash

#Wait for backend to come up
sleep 10

service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640

cd /worker

wget $BACKEND:63658/workers/script.py -O worker.py

python -u /worker/worker.py --backend $BACKEND:63658 --capabilities mininet --maxidletime $IDLE --no-clear-tmp-dir

bash

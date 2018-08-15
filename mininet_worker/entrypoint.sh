#!/bin/bash

#Wait for backend to come up
sleep 10

service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640

python -u /worker/worker.py --backend maci-backend:63658 --maxidletime -1 --capabilities mininet --no-clear-tmp-dir

bash

#!/bin/bash

# We have to install all required kernel modules at runtime...
apt-get install -y linux-modules-extra-`uname -r`

service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640

wget $BACKEND:63658/workers/script.py -O /worker/worker.py
python -u /worker/worker.py --backend $BACKEND:63658 --capabilities mininet-wifi --maxidletime $IDLE --no-clear-tmp-dir

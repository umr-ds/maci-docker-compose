### CFG int wifi_mode "Wi-Fi Mode (a=1, b=2, g=3, n=4, ac=5)"

import framework
import os
import re

from mininet.net import Mininet

def iperf(source, destination):
  destination.cmd('iperf -s -i 1 -y C > server.log &')
  source.cmd('iperf -c ' + str(destination.IP()) + ' -t 10 > client.log')
  framework.addLogfile("server.log")
  framework.addLogfile("client.log")

  server = open('server.log', 'r')
  bwsamples = []
  minTimestamp = None
  for line in server:
    # 20160622002425,10.0.0.2,5001,10.0.0.1,39345,4,0.0-1.0,14280,114240
    matchObj = re.match(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)', line, re.M)
    if matchObj:
        timestamp = float(matchObj.group(1))
        bwsample = float(matchObj.group(9)) / 1000.0 / 1000.0 # bits per second -> MBit
        bwsamples.append(bwsample)
        if minTimestamp is None:
            minTimestamp = timestamp
        framework.record("iperf_mbit_over_time", bwsample, timestamp - minTimestamp)
  framework.record("iperf_mbit_avg", sum(bwsamples) / len(bwsamples), offset=5)

if __name__ == '__main__':
  # Sometimes, old Minint instances crash.
  # We make sure that this does not crash following experiments on the same worker.
  os.system("mn -c")
  framework.start()

  net = Mininet()

  sta1 = net.addStation('sta1')
  sta2 = net.addStation('sta2')
  sta3 = net.addStation('sta3')

  net.configureWifiNodes()

  m = {{wifi_mode}}

  if m == 1:
    m = 'a'
  elif m == 2:
    m = 'b'
  elif m == 3:
    m = 'g'
  elif m == 4:
    m = 'n'
  elif m == 5:
    m = 'ac'

  net.addHoc(sta1, ssid='adhocNet', mode=m)
  net.addHoc(sta2, ssid='adhocNet', mode=m)
  net.addHoc(sta3, ssid='adhocNet', mode=m)

  net.build()

  h1 = net.get('sta1')
  h2 = net.get('sta3')

  iperf(h1, h2)

  net.stop()
  framework.stop()
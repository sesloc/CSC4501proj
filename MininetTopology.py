#!/usr/bin/python

import os, sys, socket, time, string                                				    #Imports
from mininet.topo import Topo									    #Topo import
from mininet.node import OVSController

net = mininet(topo = topo, controller = OVSController)						    #Setting controller 
class SingleSwitchTopo(Topo):									    #"Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        for h in range(n):									    #Each host gets 50%/n of system CPU
            host = self.addHost('h%s' % (h + 1), cpu=.5/n)
	    #10 Mbps, 5ms delay, 10% loss, 1000 packet queue
            self.addLink(host, switch, bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)

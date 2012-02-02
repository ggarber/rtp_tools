#!/usr/bin/env python

import argparse
import struct
from datetime import datetime
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol

begin = -1

class Receiver(DatagramProtocol):
    def datagramReceived(self, data, (host, port)):
        global begin
        if begin == -1:
            begin = datetime.now()
        timestamp = (datetime.now() - begin).microseconds/1000

	print struct.pack('i', len(data)),
	print struct.pack('i', timestamp),
	print data,

parser = argparse.ArgumentParser(description='Record received rtp traffic.')
parser.add_argument('-p', '--port', type=int, dest='port',
    default=7778, help='listening port')

args = parser.parse_args()

reactor.listenUDP(args.port, Receiver())
reactor.run()


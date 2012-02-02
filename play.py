#!/usr/bin/env python

import sys
import argparse
from datetime import datetime, timedelta
import util
import socket

parser = argparse.ArgumentParser(description='Record received rtp traffic.')
parser.add_argument('-p', '--port', type=int, dest='port',
    default=7778, help='listening port')
args = parser.parse_args()

input = sys.stdin
packer = util.packer()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', args.port))

#Wait until receiving a packet to configure the destination
data, addr = sock.recvfrom(1024)
print 'Connected to %s' % str(addr)
#addr = ('127.0.0.1', 7778)
begin = datetime.now()

while True:
    data = input.read(8)
    if not data:
        break
    length, timestamp = packer.unpack(data)

    util.wait_till(begin + timedelta(0, 0, 0, timestamp))
    
    data = input.read(length)
    sock.sendto(data, addr)


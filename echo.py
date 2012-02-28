#!/usr/bin/env python

import sys
import argparse
from datetime import datetime, timedelta
import socket

parser = argparse.ArgumentParser(description='Record received rtp traffic.')
parser.add_argument('-p', '--port', type=int, dest='port',
    default=7778, help='listening port')
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', args.port))

#Wait until receiving a packet to configure the destination
data, addr = sock.recvfrom(1024)
print 'Connected to %s' % str(addr)
#addr = ('127.0.0.1', 7778)
begin = datetime.now()

while True:
    data = sock.recv(1024)
    if not data:
        break
    
    sock.sendto(data, addr)


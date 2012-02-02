#!/usr/bin/env python

import sys
import argparse
from datetime import datetime, timedelta
import struct
import socket

parser = argparse.ArgumentParser(description='Record received rtp traffic.')
parser.add_argument('-p', '--port', type=int, dest='port',
    default=7778, help='listening port')

args = parser.parse_args()

input = sys.stdin
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('0.0.0.0', args.port))

#Wait until receiving a packet to configure the destination
data, addr = sock.recvfrom(1024)
#addr = ('127.0.0.1', 7778)
begin = datetime.now()

while True:
    data = input.read(4)
    if not data:
        break
    length = struct.unpack('i', data)[0]
    timestamp = struct.unpack('i', input.read(4))[0]

    wait_till(begin + timedelta(0, 0, 0, timestamp))

    data = input.read(length)
    socket.sendto(data, addr)



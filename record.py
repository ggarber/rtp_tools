#!/usr/bin/env python

import sys
import argparse
import socket
from datetime import datetime
import util

parser = argparse.ArgumentParser(description='Record received rtp traffic.')
parser.add_argument('-p', '--port', type=int, dest='port',
    default=7778, help='listening port')
args = parser.parse_args()

output = sys.stdout
packer = util.packer()
begin = -1
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', args.port))

while True:
    data = sock.recv(1024)

    if begin == -1:
        begin = datetime.now()
    timestamp = (datetime.now() - begin).total_seconds() * 1000

    output.write(packer.pack(len(data), timestamp))
    output.write(data)
    output.flush()


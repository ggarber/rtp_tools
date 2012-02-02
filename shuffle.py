#!/usr/bin/env python

import sys
import argparse
from datetime import datetime, timedelta
import struct
import random

input = sys.stdin
output = sys.stdout

DEFAULT_LOSS = 0.05
DEFAULT_JITTER = 10 #msecs

parser = argparse.ArgumentParser(description='Suffle rtp file including packet loss and jitter.')
parser.add_argument('-l', '--loss', dest='loss',
    default=DEFAULT_LOSS, help='packet loss')
parser.add_argument('-j', '--jitter', dest='jitter',
    default=DEFAULT_JITTER, help='jitter')

args = parser.parse_args()

begin = datetime.now()

while True:
    data = input.read(4)
    if not data:
        break
    length = struct.unpack('i', data)[0]
    timestamp = struct.unpack('i', input.read(4))[0]
    data = input.read(length)

    discard = random.random() <= args.loss
    delay = random.uniform(-1 * args.jitter, args.jitter)

    if discard:
        continue
    if delay > timestamp:
        timestamp = 0

    output.write(struct.pack('i', length))
    output.write(struct.pack('i', timestamp + delay))
    output.write(data)



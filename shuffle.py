#!/usr/bin/env python

import sys
import argparse
from datetime import datetime, timedelta
import util
import random

DEFAULT_LOSS = 0.05
DEFAULT_JITTER = 10 #msecs

parser = argparse.ArgumentParser(description='Suffle rtp file including packet loss and jitter.')
parser.add_argument('-l', '--loss', type=float, dest='loss',
    default=DEFAULT_LOSS, help='packet loss')
parser.add_argument('-j', '--jitter', type=int, dest='jitter',
    default=DEFAULT_JITTER, help='jitter')
args = parser.parse_args()

input = sys.stdin
output = sys.stdout
packer = util.packer()
begin = datetime.now()

while True:
    data = input.read(8)
    if not data:
        break
    length, timestamp = packer.unpack(data)
    data = input.read(length)

    discard = random.random() <= args.loss
    delay = random.randint(-1 * args.jitter, args.jitter)

    if discard:
        continue
    if delay < -1 * timestamp:
        delay = -1 * timestamp

    output.write(packer.pack(length, timestamp + delay))
    output.write(data)


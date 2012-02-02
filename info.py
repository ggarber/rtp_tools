#!/usr/bin/env python

import sys
import argparse
import util

parser = argparse.ArgumentParser(description='Info on recorded rtp traffic.')
args = parser.parse_args()

input = sys.stdin
packer = util.packer()
count = 0

while True:
    data = input.read(8)
    if not data:
        break
    length, timestamp = packer.unpack(data)
    data = input.read(length)

    count += 1

print 'Count: %d, Duration: %d msecs' % (count, timestamp)



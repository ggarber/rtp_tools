#!/usr/bin/env python

import sys
import argparse
import struct

input = sys.stdin

parser = argparse.ArgumentParser(description='Info on recorded rtp traffic.')

args = parser.parse_args()

count = 0
while True:
    data = input.read(4)
    if not data:
        break
    length = struct.unpack('i', data)[0]
    timestamp = struct.unpack('i', input.read(4))[0]
    data = input.read(length)

    count += 1

print "Count: %d" % count



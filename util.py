import time
from datetime import datetime
import struct

def packer():
    return struct.Struct('!II')

def wait_till(till):
    while True:
        seconds = (till - datetime.now()).total_seconds()
        if seconds <= 0:
            break 
        time.sleep(seconds) 


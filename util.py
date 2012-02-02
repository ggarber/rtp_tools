import time
from datetime import datetime
import struct

def packer():
    return struct.Struct('!II')

def wait_till(till):
    while datetime.now() < till:
        time.sleep(0.05) # 50 msecs
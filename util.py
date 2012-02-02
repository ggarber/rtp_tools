import time
from datetime import datetime

def wait_till(till):
    while datetime.now() > till:
        time.sleep(0.05) # 50 msecs
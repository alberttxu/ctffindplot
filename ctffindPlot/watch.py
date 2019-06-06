from os.path import getsize
import time

def isReady(filename):
    timeout = 10
    size = getsize(filename)
    i = 0
    while size == 0:
        time.sleep(1)
        size = getsize(filename)
        i += 1
        if i == timeout:
            print('watching %s timed out after 10 sec' % filename)
            return False
    time.sleep(0.1)
    while getsize(filename) - size:
        size = getsize(filename)
        time.sleep(1)
    return True


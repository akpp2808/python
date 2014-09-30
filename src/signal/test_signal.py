# -*- coding: utf-8 -*-
"""
Created on Dec 22, 2013
filedesc:
@author: serg
"""

import signal, os
import time

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")


# def sleep(time):
#     time.sleep
# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

print 1
time.sleep(6)
print 2
# This open() may hang indefinitely
# fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm
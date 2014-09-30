# -*- coding: utf-8 -*-
"""
Created on Jan 5, 2014
filedesc:
@author: serg
"""

import time
import signal
import gevent
from gevent_utils import BlockingDetector
from gevent import monkey
monkey.patch_all()



#     def __call__(self, *args):
#         start = time.time()
#         # get the old SIGALRM handler
#         old = signal.signal(signal.SIGALRM, self.handler)
#         # set the alarm
#         signal.alarm(self.timeout)
# 
#         #2 - start greenlet timeout
#         timer = Timeout(self.timeout)
#         timer.start()
#         try:
#             result = self.function(*args)
#         finally:
#             # restore existing SIGALRM handler
#             signal.signal(signal.SIGALRM, old)
#             timer.cancel()
#         signal.alarm(0)
#         end = time.time()
#         return result



def error_handler(signum, frame):
        print 'timeout::'
        raise GeneratorExit('Timeout Expired')

TIME = 3
def call_with_timeout(fn):
    def wrapped(*args, **kwargs):
        old = signal.signal(signal.SIGALRM, error_handler)
        signal.alarm(TIME)
        try:
            return fn(*args, **kwargs)
        finally:
            signal.signal(signal.SIGALRM, old)
    return wrapped


def call_with_timeout2(fn):
    def wrapped(*args, **kwargs):
        detector_greenlet = gevent.spawn(BlockingDetector(timeout=TIME))
        gevent.sleep()
        try:
            return fn(*args, **kwargs)
        finally:
            detector_greenlet.kill()
    return wrapped



def call_with_timeout(fn):
    def wrapped(*args, **kwargs):
        detector_greenlet = gevent.spawn(BlockingDetector(timeout=3))
        gevent.sleep()
        try:
            print 'try'
            return fn(*args, **kwargs)
        finally:
            detector_greenlet.kill()
    return wrapped


# @call_with_timeout
def sleep():
    print 'start'
    while True:
        pass
#     time.sleep(15)
    print 'end'

sleep = call_with_timeout(sleep)
sleep()



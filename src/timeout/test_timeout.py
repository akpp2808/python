# -*- coding: utf-8 -*-
"""
Created on Dec 25, 2013
filedesc:
@author: serg
"""

from timeout import call_with_timeout
import time
from gevent.timeout import Timeout


from gevent import monkey
import gevent
monkey.patch_all()

_time = 3
DEFAULT_TIMEOUT = 5


class _call_with_timeout:
    def __init__(self, function, timeout=DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.function = function

    def __call__(self, *args):
        timer = Timeout(self.timeout)
        timer.start()
        try:
            result = self.function(*args)
        finally:
            timer.cancel()
        return result

# def _call_with_timeout(fn):
#     timer = Timeout(_time)
#     timer.start()
#     try:
# #         return fn
#         return call_with_timeout(fn, _time)
#     finally:
#         timer.cancel()


def my_funct():
#     timer = Timeout(_time)
#     timer.start()

    start = time.time()
    print 'start'
    time.sleep(5)
#     time.sleep(5)
#     gevent.sleep(5)
    end = time.time()
    print 'finish', end - start


# my_funct = call_with_timeout(my_funct, _time)
# my_funct = _call_with_timeout(my_funct, _time)
my_funct()

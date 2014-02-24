# -*- coding: utf-8 -*-
"""
Created on Dec 22, 2013
filedesc:
@author: sergey.g
"""

import unittest
import time

from functools import wraps
import errno
import os
import signal
import time
import xmlrunner
import sys
import pytest
# from timeout import timeout, call_with_timeout
from timeout_decorator import timeout_decorator


from gevent import monkey
# from noodles.utils.timeout import _call_with_timeout
from utils.timeout import timeout
import gevent
from gevent.timeout import Timeout
from noodles.utils.timeout import _call_with_timeout
from gevent_utils import BlockingDetector
monkey.patch_all()

from functools import wraps
import errno
import os
import signal


from multiprocessing import Process

class TimedOutExc(Exception):
    """
    Raised when a timeout happens
    """

def timeout(timeout):
    """
    Return a decorator that raises a TimedOutExc exception
    after timeout seconds, if the decorated function did not return.
    """

    def decorate(f):

        def handler(signum, frame):
            raise TimedOutExc()

        def new_f(*args, **kwargs):

            old_handler = signal.signal(signal.SIGALRM, handler)
            signal.alarm(timeout)

            result = f(*args, **kwargs)  # f() always returns, in this scheme

            signal.signal(signal.SIGALRM, old_handler)  # Old signal handler is restored
            signal.alarm(0)  # Alarm removed

            return result

        new_f.func_name = f.func_name
        return new_f

    return decorate



from functools import wraps
from multiprocessing import Process

class TimeoutError(Exception):
    pass

def timeout(seconds=5, error_message="Timeout"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            process = Process(target=func, args=args, kwargs=kwargs)
            process.start()
            process.join(seconds)
            if process.is_alive():
                process.terminate()
                raise TimeoutError(error_message)

        return wraps(func)(wrapper)
    return decorator

# @timeout(3)
def long_time():
    print 'long_time',
    while True:
        pass

TIME = 3
class _call_with_timeout:
    def __init__(self, function, timeout=5):
        self.timeout = timeout
        self.function = function

    def __call__(self, *args, **kwargs):
        print '_call_with_timeout:'
        detector_greenlet = gevent.spawn(BlockingDetector(timeout=self.timeout))
        gevent.sleep()

        time.sleep(10)
#         self.assertRaises(AlarmInterrupt, time.sleep, 1)
        detector_greenlet.kill()
def call_with_timeout(f):

# long_time = _call_with_timeout(long_time, 1)
detector_greenlet = gevent.spawn(BlockingDetector(timeout=TIME))
gevent.sleep()
long_time()
detector_greenlet.kill()

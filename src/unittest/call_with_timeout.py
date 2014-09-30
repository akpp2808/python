# -*- coding: utf-8 -*-
"""
Created on Jan 5, 2014
filedesc:
@author: serg
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
import gevent
from gevent_utils import BlockingDetector


def call_with_timeout2(fn):
    def wrapped(*args, **kwargs):
        detector_greenlet = gevent.spawn(BlockingDetector(timeout=3))
        gevent.sleep()
        try:
            print 'call_with_timeout2'
            return fn(*args, **kwargs)
        finally:
            detector_greenlet.kill()
    return wrapped

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


class Test(unittest.TestCase):

    def test_main(self):
        print 'test_main'
        time.sleep(10)
#         for i in range(5):
#             print 'i', i
#             time.sleep(1)
        print 'finish'

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(
        Test('test_main'),
    )
    report = './'
    runner = xmlrunner.XMLTestRunner(output=report,
                                     stream=sys.stderr,
                                     verbosity=2)
    for test in suite._tests:
        suite._tests[suite._tests.index(test)] = call_with_timeout2(test)
    runner.run(suite)

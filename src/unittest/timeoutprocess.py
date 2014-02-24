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
from noodles.utils.timeout import _call_with_timeout
from utils.timeout import timeout
import gevent
from gevent.timeout import Timeout
monkey.patch_all()

from functools import wraps
import errno
import os
import signal
import timeoutprocess


# @timeout_decorator.timeout(3)
# @timeout(5)
def test_timeout():
    i = 0

    print 'test_timeout'
    while i < 10:
        time.sleep(0.5)
        i += 1
        try:
            while 1:
                pass
#                 time.sleep(1)
#                 print 'sleep', time.time()
#                 pass
#             pass
            #1
            gevent.sleep(20)
            #2
#             time.sleep(500)
        except Exception, e:
            now = time.time()
            print 'except', i, e
            continue
        print 'finish test_timeout'

# test_timeout = _call_with_timeout(test_timeout, 3)
timeoutprocess.TimeoutProcess(test_timeout, 10)


# 
# class Test(unittest.TestCase):
# #     @timed
# #     @pytest.mark.timeout(3)
# #     @timeout(timeout=2)
# #     @timeout()
# #     @timeout_decorator.timeout(2)
#     def test_main(self):
#         i = 0
#         print 'main'
# 
#         while i < 10:
#             time.sleep(1)
#             i += 1
#             try:
#                 while 1:
#                     time.sleep(0.1)
#                 raise Exception(111, 'bla')
#             except Exception, e:
#                 now = time.time()
#                 print 'except', timeout, e
# #                 print 'time', now - start
#                 continue
# #         time.sleep(10)
# #         for i in range(5):
# #             print 'i', i
# #             time.sleep(1)
#         print 'finish'
# 
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(
#         Test('test_main'),
#     )
#     report = './'
#     runner = xmlrunner.XMLTestRunner(output=report,
#                                      stream=sys.stderr,
#                                      verbosity=2)
# 
#     for test in suite._tests:
# 
# #         print 'test', test, [test]
# #         return_later_or_timeout = call_with_timeout(test, 4)
#         suite._tests[suite._tests.index(test)] = call_with_timeout(test, 3)


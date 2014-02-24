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
from timeout import timeout, call_with_timeout
from timeout_decorator import timeout_decorator



class Test(unittest.TestCase):
#     @timed
#     @pytest.mark.timeout(3)
#     @timeout(timeout=2)
#     @timeout()
#     @timeout_decorator.timeout(2)
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
        suite._tests[suite._tests.index(test)] = call_with_timeout(test, 4)
    runner.run(suite)

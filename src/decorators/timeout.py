# -*- coding: utf-8 -*-
"""
Created on Dec 22, 2013
filedesc:
@author: serg
"""

from functools import wraps
import errno
import os
import signal
import time
import pytest


class TimeoutError(Exception):
    pass


def timeout(seconds=2, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

# @timeout()
# @pytest.mark.timeout(timeout=2)
def test_funct():
    for i in range(5):
        print 'i', i
        time.sleep(1)

# print pytest.mark.timeout(timeout=5, method=test_funct)

test_funct = timeout()(test_funct)
# f()
test_funct()

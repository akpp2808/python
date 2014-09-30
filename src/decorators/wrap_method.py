# -*- coding: utf-8 -*-
"""
Created on Jan 12, 2014
filedesc:
@author: serg
"""
from functools import wraps


def wrap_error(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception, e:
            print 'error:', e

    return wrapped


class Foo():
    @wrap_error
    def test(self, raise_err=True):
        result = None
        if raise_err:
            result = 1 / 0
        else:
            result = 1
        return result

f = Foo()
print f.test(False)

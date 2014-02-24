# -*- coding: utf-8 -*-
"""
Created on Jan 21, 2014
filedesc:
@author: serg
"""


def get_attrs(attrs):
    __all = {'a': lambda: 1,
             'b': lambda: 2,
             'c': lambda: 3,
             }
    result = {}
    for a in attrs:
        fn = __all[a]
        result[a] = fn()
    return result
    return {a: () for a in attrs}


print get_attrs(['a', 'c'])


def get_a(False): pass
def get_b(True): pass

fn = [get_a, get_b][True]
print 'fn', fn
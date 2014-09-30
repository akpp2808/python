# -*- coding: utf-8 -*-
"""
Created on Jul 30, 2014
filedesc:
@author: serg
"""

import inspect
# trigger_method_name = inspect.getframeinfo(inspect.currentframe().f_back)[2]
# print 'trigger_method_name', trigger_method_name


def b():
    print inspect.getframeinfo(inspect.currentframe().f_back)
    return


def a():
    b()

a()
# -*- coding: utf-8 -*-
"""
Created on Jul 3, 2013
filedesc:
@author: serg

"""


class A:
    d = 2

    def __get__(self, name):
        raise Exception('Cannot get property %s' % name)



a = A()
#a.d = 33

print a.d
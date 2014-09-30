# -*- coding: utf-8 -*-
"""
Created on Aug 9, 2014
filedesc:
@author: serg
"""


class A:
    value = 10

class B:
    value = 5

a = A()
b = B()

print 'a', a.value
print 'b', b.value


print max([a, b], key=lambda a: a.value)
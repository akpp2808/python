# -*- coding: utf-8 -*-
"""
Created on Jun 13, 2013
filedesc:
@author: serg

"""
import time

l = []


x = lambda: l.append(time.time())

print 'l', l
x()
print 'l', l
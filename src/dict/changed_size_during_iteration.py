# -*- coding: utf-8 -*-
"""
Created on Dec 30, 2013
filedesc:
@author: serg
"""

d = {'a': [1], 'b': [1, 2], 'c': [], 'd': []}

# for i in d:
for i in d.keys():
    print 'i', i, d[i]
    if not d[i]:
        d.pop(i)

print 'd', d

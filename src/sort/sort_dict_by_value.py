# -*- coding: utf-8 -*-
"""
Created on Jun 9, 2013
filedesc:
@author: serg

"""
import time

time.time()
a = {'time': 1, 'name': 'a'}
b = {'time': 2, 'name': 'b'}
c = {'time': 3, 'name': 'c'}
d = {'time': 5, 'name': 'd'}


dicts_list = [b, c, d, a]
#first.sort(cmp=compare, key=None, reverse=False)
#dicts_list.sort(key=lambda a: a.get('time'))
# dicts_list.sort(key=lambda a: a.get('time'))

print dicts_list


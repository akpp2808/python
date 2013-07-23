# -*- coding: utf-8 -*-
"""
Created on Jun 23, 2013
filedesc:
@author: serg

"""


import redis
rc = redis.Redis(db=80)
key = 'mylist'
rc.delete(key)


for i in range(2):
    text = 'msg: %s' % i
    rc.rpush(key, text)

l = rc.lrange(key, 0, -1)
print 'all', len(l), l

backlog = 5
l = rc.lrange(key, 0, -1 - backlog)
print 'save', len(l), l
rc.rpush(key, 'bla')

rc.ltrim(key, len(l), -1)

l = rc.lrange(key, 0, -1)
print 'backlog', len(l), l




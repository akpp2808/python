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


for i in range(11):
    text = 'msg: %s' % i
    rc.lpush(key, text)

l = rc.lrange(key, 0, -1)
print 'all', len(l), l

backlog = 5
l = rc.lrange(key, -backlog, -1)
print 'save', len(l), l
rc.lpush(key, 'bla')

rc.ltrim(key, 0, -1-backlog)

l = rc.lrange(key, 0, -1)
print 'backlog', len(l), l




#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Dec 9, 2011

@author: serg
'''

import redis
REDIS_HOST = 'localhost'
RDB = '1'
#rc = redis.Redis(host=REDIS_HOST, port=6379, db=RDB)
rc = redis.Redis()
channel = 'ASD'
pubsub = rc.pubsub()
pubsub.subscribe(channel)

print 'run2'
for msg in pubsub.listen():
    print msg

print 'run'
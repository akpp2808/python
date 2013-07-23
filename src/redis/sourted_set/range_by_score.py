# -*- coding: utf-8 -*-
"""
Created on Jun 10, 2013
filedesc:
@author: serg

"""
import redis, time
NAME = 'log'


rc = redis.Redis(db=80)
rc.delete(NAME)

now = time.time()


msg_type = 0
system_type = 1
meta_type = 2
rc.zadd(NAME, 'meta: 1', meta_type)
rc.zadd(NAME, 'msg: hello', msg_type)  # args params
rc.zadd(NAME, 'msg: world', msg_type)
rc.zadd(NAME, 'system: 1', system_type)
rc.zadd(NAME, 'msg: hi', msg_type)
rc.zadd(NAME, 'msg: bla', msg_type)
#rc.zadd(NAME, 'msg: 1', msg_type)
#rc.zadd(NAME, 'msg: 2', msg_type)
#rc.zadd(NAME, 'msg: 3', msg_type)
#rc.zadd(NAME, 'msg: 4', msg_type)

#without limit
_all = rc.zrangebyscore(NAME, 0, 2)
print  'all', len(_all), _all
admin = rc.zrangebyscore(NAME, 0, 2)
print  'admin', len(admin), admin
user = rc.zrangebyscore(NAME, 0, 0)
print  'user', len(user), user

meta = rc.zrangebyscore(NAME, 1, 2)
print  'meta', len(meta), meta



#_all = rc.zrange(NAME, -7, -1)
#print rc.zrange(NAME, 0, -1, withscores=True)
#return only msg type
#_all = rc.zrangebyscore(NAME, 0, 0)
#print  'all', len(_all), all
#_all = rc.zrangebyscore(NAME, 0, 2)
#print  'all', len(_all), _all
#admin = rc.zrangebyscore(NAME, 0, 2, 0, 5)
#print  'admin', len(admin), admin
#user = rc.zrangebyscore(NAME, 0, 0, 0, 20)
#print  'user', len(user), user
#
#meta = rc.zrangebyscore(NAME, 1, 2, 0, 5)
#print  'meta', len(meta), meta
#return all msg types
#admin = rc.zrangebyscore(NAME, 0, 2, 0, 1)
#print 'admin', len(admin), admin
#redis.exceptions.RedisError: ``start`` and ``num`` must both be specified
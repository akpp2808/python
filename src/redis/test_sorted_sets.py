# -*- coding: utf-8 -*-
'''
Created on May 19, 2013

@author: serg
'''
import json

NAME = 'users'
#NAME = 'talk:783bc77a18509089774a3729cb83ef0e'
import redis
rc = redis.Redis(db=80)
rc.delete(NAME)
# устанавливаем значения

msg = json.dumps({"name": "Sergey",
                  "text": "2",
                  "su": True,
                  "mt": None,
                  "tm": 1368917328.533533,
                  "r#": "783bc77a18509089774a3729cb83ef0e",
                  "tid": "136891732852982838",
                  "u#": "2aa9242a37694d81b4c620fe38957e1a"})

rc.zadd(NAME, 'a', 2)  # args params
rc.zadd(NAME, 'b', 12)
rc.zadd(NAME, 'b', 14)
rc.zadd(NAME, 'c', 1.3)
#rc.zadd(NAME, a=11)  # kwargs params


#print rc.zrange(NAME, 0, -1)  # keys
#print rc.zrange(NAME, 0, -1, withscores=True)  # with value
start, end = 0, -1
desc = True
withscores = False
withscores = True
score_cast_func = int  # ???
#for key, val in  rc.zrange(NAME, start, end, desc, withscores, score_cast_func):
#    print key, val
#print rc.zrange(NAME, start, end, desc, withscores)
#users =  rc.zrange(NAME, start, end, desc, withscores, score_cast_func)
users =  rc.zrange(NAME, start, end, desc, withscores, score_cast_func)
#print 'tuple', users  # list of tuple [('b', 12.0), ('a', 11.0), ('c', 1.3)]
print dict(users)   # dict key: value {'a': 11.0, 'c': 1.3, 'b': 12.0}
print len(users)
print rc.zcard(NAME)  # Get the number of members in a sorted set
print rc.zcount(NAME, 2, 12)  # {'c': 1.3}


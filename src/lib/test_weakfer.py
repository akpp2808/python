# -*- coding: utf-8 -*-
'''
weakref — Weak references
link: http://docs.python.org/2/library/weakref.html
'''


import unittest
from weakref import WeakSet, WeakValueDictionary
import redis
import weakref
rc = redis.Redis(db=80)
rc.set('a', 1)
#print 'a', rc.get('a')
class Object:
    pass

obj = Object()
obj2 = Object()

ws = WeakSet()
ws.add(obj)
#print dir(ws)
#print 'len()', len(ws)



o = Object()
#print o

class TestWeakSet(unittest.TestCase):
    def test_len(self):
        obj = Object()
        obj2 = Object()
        ws = WeakSet([obj])
        self.assertIn(obj, ws)
        self.assertEqual(len(ws), 1)
        ws.add(obj2)
        self.assertEqual(len(ws), 2)
        self.assertIn(obj2, ws)
        del obj
        self.assertEqual(len(ws), 1)
        self.assertIn(obj2, ws)


a = Object()
b = Object()
c = Object()
d = Object()

#ONLINE_USERS.add()
connections = WeakSet([a, b])
print 'USER_SESSIONS',  len(connections)
c = connections
print c 

users = WeakSet([connections])  # list of user sessions
#u = weakref.ref(users)  # list of user sessions
#print 'ONLINE_USERS', len(users)
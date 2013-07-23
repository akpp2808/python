# -*- coding: utf-8 -*-
import redis
import json
rc = redis.Redis(db=80)

d = {'a': 1, 'b': 2}


#HSET name, key, value - установить значение поля
#rc.hset('user', 'login', 'test_user')
#rc.hset('user', 'login', 'test_user2')
#print rc.hget('user', 'login')
#rc.hset('user', 'password', '123456')
#print rc.hget('user', 'password')

# установить значения нескольких полей
#HMSET name key value [key1 value1 [key2 value2]]

#data = {'pb': True, 'ur': 0, 'in': ['c6f4a8b262ca4ac084272e0c782757ef']}
#rc.hset('rooms', 'room1', json.dumps(data))
#print rc.hget('data', 'in'), type(rc.hget('data', 'in'))
data = {'id': '123', 'password': '123456', 'dob': '01/07/1987', 'id': 124, 'unread': 0}
rc.hmset('user1', data)
#print rc.hget('user1', 'password')
#print rc.hget('user', 'dob')


items = [1, 2, 3, 4]
#for pair in data.iteritems():
#    items.extend(pair)

#print 'item', items, type(items)
#rc.execute_command('HMSET', 'bla', *items)

#print rc.hget('bla', 1)
#for i in data.iteritems():
#    print i

print rc.hgetall('user1')
rc.hincrby('user1', 'unread', 5)
#rc.hset('user1', 'password', 456789)
print rc.hgetall('user1')
#print rc.hmget('user1', 'password')
#print rc.hdel('user1', 'id')
#print rc.hgetall('user1')
#print rc.delete('user1', 'id')
#print rc.hgetall('user1')

#l = rc.hget('rooms', 'in')

#print l
'''
Created on Dec 9, 2011

@author: serg
'''
import redis, json, time
REDIS_HOST = 'localhost'
RDB = '80'
rc = redis.Redis(host=REDIS_HOST, port=6379, db=RDB)

channel = 'ASD'
#data = {'action':'a1'}
message = time.strftime('%s')
data = {u'action': 'chats:addmessage', u'data': {u'id': u'029b897521cb3c885be0284ef22849ac', u'attr': {u'name': u'Guest_14', u'userid': 14, u'time': u'1323423809', u'message': message, u'unread': 1, u'id': 1250,u'type':'msg'}}}
msg = json.dumps(data)
#print rc.publish(channel, msg), message


#{key: value}
user_id = 36

data = {'action': 'chats:update','data':{
    'id': user_id
}}


channel = '80:subscribe_to_online_users_list'

#print rc.publish(channel,json.dumps(data)) 
print rc.publish(channel,'a') 
'''
Created on Dec 9, 2011

@author: serg
'''
import redis, json, time
rc = redis.Redis()
channel = 'ASD'
#data = {'action':'a1'}
message = time.strftime('%s')
data = {u'action': 'chats:addmessage', u'data': {u'id': u'029b897521cb3c885be0284ef22849ac', u'attr': {u'name': u'Guest_14', u'userid': 14, u'time': u'1323423809', u'message': message, u'unread': 1, u'id': 1250,u'type':'msg'}}}
msg = json.dumps(data)
print rc.publish(channel, msg), message


#{key: value}
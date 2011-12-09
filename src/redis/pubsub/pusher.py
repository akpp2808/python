'''
Created on Dec 9, 2011

@author: serg
'''
import redis, json
rc = redis.Redis()
channel = 'ASD1'
data = {'action':'a'}
message = json.dumps(data)
rc.publish(channel, message)
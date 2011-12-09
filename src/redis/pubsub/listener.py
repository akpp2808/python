'''
Created on Dec 9, 2011

@author: serg
'''

import redis
rc = redis.Redis()
channel = 'ASD1'
pubsub = rc.pubsub()
pubsub.subscribe(channel)

for msg in pubsub.listen():
    print msg
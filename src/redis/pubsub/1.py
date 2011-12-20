import redis
rc = redis.Redis()
#print dir(redis)

#rc.set('foo','bar')
#print rc.get('foo')
#print dir(rc)
pubsub = rc.pubsub()
#print dir(pubsub)
print pubsub.channels


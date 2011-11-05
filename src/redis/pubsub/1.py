import redis
rc = redis.Redis()
#print dir(redis)

rc.set('foo','bar')
print rc.get('foo')
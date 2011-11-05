import redis

rc = redis.Redis()
rc.sadd('myset2','4')
rc.sadd('myset2','5')
rc.sadd('myset2','7')

print rc.smembers('myset2')         #set(['5', '4', '7'])

print rc.sismember('myset2','5')    #True
print rc.sismember('myset2','8')    #False
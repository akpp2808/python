'''
Created on May 19, 2013

@author: serg
'''
import json
import time
import redis

NAMESPACE = 'log'
TRESHOLD = 5  # seconds
BACKUP = 'backup'
QUANT = 10  # min items to store
MINAMOUNT = 20  # msg without store

rc = redis.Redis()
rc.delete(NAMESPACE)
rc.delete(BACKUP)




msg = json.dumps({"name": "Sergey",
                  "text": "2",
                  "su": True,
                  "mt": None,
                  "tm": 1368917328.533533,
                  "r#": "783bc77a18509089774a3729cb83ef0e",
                  "tid": "136891732852982838",
                  "u#": "2aa9242a37694d81b4c620fe38957e1a"})

#rc.rpush(NAMESPACE, msg)  # Append one values to a list
#rc.rpush(NAMESPACE, msg)
for i in range(25):
    print 'push', rc.lpush(NAMESPACE, 'msg%s' % i)
#rc.rpush(NAMESPACE, 'msg3')

start, end = 0, -1
print rc.llen(NAMESPACE)  # Get the length of a list
#print rc.lrange(NAMESPACE, start, end)  # Get a range of elements from a list


#all = reversed(rc.lrange(NAMESPACE, start, end))
all = rc.lrange(NAMESPACE, start, end)
#print 'all', all

for m in all:
#    print json.loads(m)
    print m


def pop():
    namespace = NAMESPACE
#    if rc.llen(namespace) > 20:
#    if MINAMOUNT + QUANT < rc.llen(namespace):
    llen = rc.llen(namespace)
    print MINAMOUNT + QUANT, llen
    if MINAMOUNT + QUANT < llen:
        while True:
#        print 'popmesg'
#        print 'pop', rc.brpop(namespace, 2)
            print 'pop', rc.rpop(namespace)
            if MINAMOUNT > rc.llen(namespace):
                print 'exit1'
                return
            pop()
        else:
            print 'else'
#def pop():
#    namespace = NAMESPACE
##    if rc.llen(namespace) > 20:
##    if MINAMOUNT + QUANT < rc.llen(namespace):
#    llen = rc.llen(namespace)
#    print MINAMOUNT + QUANT, llen
#    if MINAMOUNT + QUANT < llen:
#        while MINAMOUNT < rc.llen(namespace):
##        print 'popmesg'
##        print 'pop', rc.brpop(namespace, 2)
#            print 'pop', rc.rpop(namespace)
#            pop()
#        else:
#            print 'else'


#    time.sleep(1)

src = NAMESPACE
dst = []


print 'process...'
while True:
    time.sleep(TRESHOLD)
    pop()
#    msg = rc.brpop(NAMESPACE, 5)
#    print 'pop', msg



#print 'src', rc.lrange(NAMESPACE, start, end)
#print 'dst', rc.lrange(BACKUP, start, end)


rc.save()






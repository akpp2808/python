'''
Created on May 19, 2013

@author: serg
'''
import unittest, redis

NAMESPACE = 'log'
TRESHOLD = 5  # seconds
BACKUP = 'backup'
QUANT = 10  # min items to store
MINAMOUNT = 20  # msg without store

rc = redis.Redis()
rc.delete(NAMESPACE)
rc.delete(BACKUP)
CNT = 100000


class Test(unittest.TestCase):
    def test_main(self):
        with rc.pipeline() as pipe:
            print 'pipe', pipe
#            print dir(pipe)

#            pipe.watch(NAMESPACE)
            pipe.multi()
            try:
                for i in range(CNT):
                    if i == 5:
                        raise Exception()
                    pipe.lpush(NAMESPACE, 'msg%s' % i)
            except:
                print 'except'
                pipe.discard()
            else:
                print 'OK'
                pipe.execute()
            finally:
                pass
#        print 'all', rc.lrange(NAMESPACE, 0, -1)
#            while True:
#                try:
#                    pipe.watch("a_hash")
#                    if pipe.exists("a_hash"):
#                        pipe.multi()
#                        pipe.hset("a_hash", "key", "value")
#                        pipe.execute()
#                    break
#                except redis.WatchError:
#                    continue
#                finally:
#                    pipe.reset()

#        for i in range(CNT):
#            rc.lpush(NAMESPACE, 'msg%s' % i)
#            print rc.zadd(NAMESPACE, 'msg%s' % i, 1)

#        rc.lrange(NAMESPACE, 0, -1)
#        print rc.llen(NAMESPACE)
#        while True:
#            res = rc.rpop(NAMESPACE)
#            if not res:
#                break




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
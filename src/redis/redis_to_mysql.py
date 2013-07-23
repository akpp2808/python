# -*- coding: utf-8 -*-
"""
Created on Jun 22, 2013
filedesc: Create Python class where the attributes is defined dynamically
@author: serg

"""
import json


class MysqStore():
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


#a = MysqStore(a=1, b=2)

#print a.a  # 1


#redis
import redis, time

#key = 'ac123456bn'  # room id + hash
room_id = 'ac123456bn'
rc = redis.Redis(db=80)
rc.delete(room_id)


def create_msg(text):
    msg = {'r#': room_id,
            'text': text,
            'mt': 1,  # message type
            'tm': time.time(),
            'name': 'test',
            'u#': '123qwe',
            }
    return json.dumps(msg)

for i in range(11):
    text = 'msg %s' % i
    msg = create_msg(text)
    rc.lpush(room_id, msg)

l = rc.lrange(room_id, 0, -1)
print len(l), l



archive = []

def callback(a, b):
    print 'here'

def log2mysql(key, backlog=5):
    pipe = rc.pipeline()
    logs = rc.lrange(key, backlog, -1)
    print 'len', len(logs)
    for raw_msg in logs:
        msg_data = json.loads(raw_msg)
#        print msg_data
#        res = msg.get('text').find('5')
        m = pipe.rpop(key)
#        print 'm', m, dir(m)
##                msg_mysql = MysqStore()
#        archive.append(m)
##                break
#        raise Exception('bla exception')
#                if res != -1:
#                    print msg.get('text')
#                    assert 0
#                pipe.lpush(NAMESPACE, 'msg%s' % i)

def archivator(key):
    pipe = rc.pipeline()
#    pipe.multi()
    print pipe
    print 'a', pipe.set('a', 2)
    print 'a', pipe.set('a1', 2)
    print 'a', pipe.set('a3', 3)

    print 'a', pipe.get('a3')
#    print 'a5', pipe.immediate_execute_command('SET', 'A', 321)
#    print 'a5', pipe.pipeline_execute_command('SET', 'A', 322)
    print 'a5', pipe.delete('A')
    print 'a5', rc.get('A')
    try:
        #save to mysql
        log2mysql(key)
    except Exception as e:
        print 'except', e
        pipe.reset()
    else:
        print 'OK'
        pipe.execute()
    finally:
        pass
    
#    print pipe.execute()

#    print 'm', m.__dict__, dir(m)
#    pipe.execute()
#    with rc.pipeline() as pipe:
#        print 'pipe', dir(pipe)
##            print dir(pipe)
#
##        pipe.watch(key)
#        pipe.multi()
#        try:
#            for raw_msg in rc.lrange(key, 0, -1):
##                    if i == 5:
##                        raise Exception()
#                msg = json.loads(raw_msg)
#                res = msg.get('text').find('5')
#                m = pipe.rpop(key)
#                print 'm', m, dir(m)
##                msg_mysql = MysqStore()
#                archive.append(m)
##                break
#                raise Exception('bla exception')
##                if res != -1:
##                    print msg.get('text')
##                    assert 0
##                pipe.lpush(NAMESPACE, 'msg%s' % i)
#        except Exception as e:
#            print 'except', e
##            pipe.discard()
#        else:
#            print 'OK'
#            pipe.execute()
#        finally:
#            pass

archivator(room_id)
l = rc.lrange(room_id, 0, -1)
print len(l), l



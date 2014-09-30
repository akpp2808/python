# -*- coding: utf-8 -*-
"""
Created on Dec 24, 2013
filedesc:
@author: serg
"""
from gevent.hub import Waiter, get_hub
from gevent import core
import time
from gevent.timeout import Timeout
import gevent
from timeout import TimeoutException
from gevent import monkey
monkey.patch_all()


seconds  = 3
timeout = Timeout(3)
timeout.start()
# timeout = Timeout.start_new(seconds)
try:
    print 'sleep'
#     gevent.sleep(10)
    time.sleep(10)
    # exception will be raised here, after *seconds* passed since start() call
finally:
    timeout.cancel()



# Timeout(0.1).start()
# time.sleep(1)
# # gevent.sleep(0.2)
# print 'finish'
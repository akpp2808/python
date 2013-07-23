'''
Created on May 22, 2013

@author: serg
'''
import time
from lib.utils import get_config, mkey
import uuid
rc = get_config('REDIS_CONN')

#-*- coding: utf-8 -*-
"""
@author: serg0987@gmail.com
"""
import unittest


class UserSession(object):
    def __init__(self):
        self.class_name = self.__class__.__name__.lower()
#    user_id = Value(str)
#    login = Value(str)  # not used
#    firstname = Value(str)
#    guestname = Value(str)
#
#    is_guest = Value(bool)
#    is_admin = Value(bool)
#    logged_in = Value(bool)
#    last_ws_session = Value(str)  # one time token id
#    logout = Value(bool)
#    operator_id = Value(int)
#    room_id = Value(str)  # chat room
#    user_agent = Value(str)
#    remote_addr = Value(str)
#
#    time_last_activity = Value(int)
#    time_start = Value(int)
#    time_end = Value(int)

    def create_session(self, kwargs={}):
        #TODO: or user built redis incr
        uid = uuid.uuid4().hex
        now = time.time()
        params = {
          'id': uid,
          'created_at': now,
                  }

        params.update(kwargs)
        collection_name = mkey(self.class_name, uid)
        rc.hmset(collection_name, params)

SESSION_MANAGER = Session()


class TestUserSession(unittest.TestCase):

    def test_main(self):
        kwargs = {
                'login': 'test_user_1235'
                }
        SESSION_MANAGER.create_session(kwargs)

if __name__ == '__main__':
    unittest.main()
# -*- coding: utf-8 -*-
"""
Created on Jul 27, 2013
filedesc:
@author: serg
"""

from redisco.containers import Hash
import unittest
import time
import redisco
import uuid
from redisco import containers
import collections

redisco.connection_setup(db=123)

class TestModel(unittest.TestCase):
    def setUp(self):
        self.client = redisco.get_client()
        self.client.flushdb()
    
    def create_model(self):
        pass
    
    def test_hash(self):
#         start_time = time.time()
#         while time.time() - start_time < 1:
            print collections.MutableMapping
            id = uuid.uuid4().hex  # @ReservedAssignment
            h = Hash(id, pipeline=True)
            h['session_id'] = uuid.uuid4().hex
            h['operator_id'] = uuid.uuid4().hex
            self.client.expire(id, 30)
            m = self.client.hgetall(id)
            
            m['session_id']
#             self.create_model()
#         else:
            print 'amount', len(self.client.keys('*'))
#             print '\n%s result: %s per second\n' % (model.__name__, len(model.all()))
        
        
        
#     test_hash()




if __name__ == "__main__":
    unittest.main()
    
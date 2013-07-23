'''
Created on Apr 6, 2013

@author: Sergey Golota

model of FIFO
'''

import unittest
from gevent.queue import JoinableQueue


class TestGeventQueue(unittest.TestCase):
    def test_main(self):
        queue = JoinableQueue()
        print dir(queue)
        queue.put(1)
        queue.put(3)
        queue.put(2)
        queue.put(6)
        print queue.qsize()

        print '1', queue.get(), queue.get()
#        print '13', len(queue.get()), '3'

#        queue.put(3)
#        queue.put(2)


if __name__ == '__main__':
    unittest.main()

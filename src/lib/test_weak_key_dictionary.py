'''
Created on Apr 6, 2013

@author: Sergey Golota
'''

import unittest
from weakref import WeakKeyDictionary


class Object:
    pass


class TestWeakKeyDictionary(unittest.TestCase):
    def test_main(self):
        d = WeakKeyDictionary()
        o = Object()
        d[o] = 'same value'
        self.assertEqual(len(d), 1)
        del o
        self.assertEqual(len(d), 0)

if __name__ == '__main__':
    unittest.main()

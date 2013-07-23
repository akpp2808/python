'''
Created on May 14, 2013

@author: serg
'''
import unittest
from functools import wraps

def action(fn):
    @wraps(fn)
    def wrapper(a):
        response = fn(a)
        return response + 1
    return wrapper

class Test(unittest.TestCase):
    def setUp(self):
        @action
        def test(x):
            if not x%2:
                return 50
            return x
        print test(2)


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
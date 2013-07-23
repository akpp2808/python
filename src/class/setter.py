'''
Created on May 13, 2013

@author: serg
'''


class A:
    def __setattr__(self, name, value):
        raise Exception('Cannot set property')



a = A()
a.d = 33

print a.d
'''
Created on May 8, 2013

@author: serg
'''


class A():
    name = 'base'
class B(A):
    pass

b = B()
print b.name
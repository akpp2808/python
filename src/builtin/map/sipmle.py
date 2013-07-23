'''
Created on May 8, 2013

@author: serg
'''


def test(x, y):
    return x * y

print map(test, [1, 4], [2, 6])  # [2, 24]

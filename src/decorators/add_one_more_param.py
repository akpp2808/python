'''
Created on Apr 25, 2013

@author: serg
'''

def add_param(funct):
    def gen(a, b):
        return funct(a, b, c=121)
    return gen


@add_param
def test(a, b, c):
    print a, b, c

test(a=1, b=3)

'''
Created on Apr 28, 2013

@author: serg
'''
from functools import wraps


def action(fn):
    @wraps(fn)
    def wrapper(a, b):
        response = fn(a, b)
        a, b = response
        return {'action': fn.__name__, 'response': {'a': a, 'b': b}}
    return wrapper

def add_param(funct):
    def gen(a, b):
        return funct(a, b, c=121)
    return gen


#@add_param
@action
def test(a, b):
    return a, b

print test(a=1, b=3)

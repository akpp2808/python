# -*- coding: utf-8 -*-
"""
Created on Jul 28, 2013
filedesc:
@author: serg
"""

class MetaClass():
    def __init__(self, **kwargs):
        print 'init base'

class Foo():
    __metaclass__ = MetaClass
    def __init__(self, **kwargs):
        print 'init foo'
        
        
f = Foo()
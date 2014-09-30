# -*- coding: utf-8 -*-
"""
Created on Dec 30, 2013
filedesc:
@author: serg
"""

import weakref, gc
from weakref import WeakValueDictionary
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # создаёт ссылку
b = A(0)                   # создаёт ссылку
c = A(5)                   # создаёт ссылку
d = weakref.WeakValueDictionary()  # словарь, использующий слабые ссылки
d['a'] = a            # не создаёт ссылки
d['b'] = b            # не создаёт ссылки
# d['primary']                # достать объект, если он все ещё "жив"
# 
# for i in d.itervaluerefs():
#     if i.key == 'b':
# #         pass
# #         d['c'] = c
#     print 'i', i.key
#     print 'i', dir(i)


min_info = {}
weakdict = WeakValueDictionary()

for k, v in {'a': 1, 'b': 0, 'c': 3}.iteritems():
    inst = A(v)
    min_info[k] = inst
    weakdict[k] = inst

print 'min_info', min_info
print 'weakdict', [x() for x in weakdict.itervaluerefs()]
print 'weakdict', weakdict.iteritems()

for x in weakdict.itervaluerefs():
    print 'x', dir(weakdict.itervaluerefs())
    

# 10
# del a                       # удалить одну ссылку
# gc.collect()                # произвести сборку мусора
# 0
# d['primary']                # запись была автоматически удалена
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     d['primary']
#   File "C:/python31/lib/weakref.py", line 46, in __getitem__
#     o = self.data[key]()
# KeyError: 'primary'
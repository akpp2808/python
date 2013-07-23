'''
Created on May 22, 2013

@author: serg
'''
import unittest

l = []


def set_idx(user_id):
    user_id = str(user_id)
    if user_id in l:
        return
    if len(l) > 1:
        l[-1] = user_id
    else:
        l.append(user_id)

#    l.append(user_id)
#    l.extend(l)
    print 'l', l


for i in [1, 1, 2, 3]:
    set_idx(i)
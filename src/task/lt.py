# -*- coding: utf-8 -*-
"""
Created on Jul 27, 2014
filedesc:
@author: serg
"""

#current_wagering_req, wagering_req_balance, instance_wagering_req
items = [
# (0, 100, 0),
(-120,  50, -50),
(-20,  50, -20),
(-50,  50, -50),
(10,  50, 10),
(0,  50, 0),
]


def take_of_le(x, total):
    """
        снимаем не больше чем есть
    """
    if x < 0:
        return x if abs(x) < total else total * -1
    else:
        return x

for i in items:
    current, total, wagering_req = i
    print 'i:', current, total, wagering_req
    print take_of_le(current, total) == wagering_req


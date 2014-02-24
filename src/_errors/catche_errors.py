# -*- coding: utf-8 -*-
"""
Created on Feb 1, 2014
filedesc:
@author: serg
"""

import time


while True:
    try:
        OperationalError()
        break
    except OperationalError, e:
        print 'er', e
        time.sleep(1)
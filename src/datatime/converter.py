# -*- coding: utf-8 -*-
"""
Created on Mar 23, 2015
filedesc:
@author: serg
"""

import time
from datetime import datetime

print int(time.time() * 1e6)
print int(time.time() * 1000000)
now = datetime.now()
print int(time.mktime(now.timetuple()) * 1e6 + now.microsecond)

# -*- coding: utf-8 -*-
"""
Created on Dec 2, 2013
filedesc:
@author: serg
"""
import re


LOGIN_PATTERN = re.compile('^[a-zA-Z0-9_.-]+$')
NAME_PATTERN = re.compile('^[\w\.\-]+$', re.UNICODE)
# EMAIL_PATTERN = re.compile('^[\w\d._-+]+$')
EMAIL_PATTERN = re.compile('^[\w\d.]+$')

#letters (a-z), numbers, and periods.
# EMAIL_PATTERN = re.compile('^[a-zA-Z0-9._%+-]+$')


print EMAIL_PATTERN.match('BLA.+')
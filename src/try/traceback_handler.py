# -*- coding: utf-8 -*-
"""
Created on Feb 24, 2014
filedesc:
@author: serg
"""

import sys

import logging

print logging

try:
    raise Exception(123, 'bla')
except:
    print logging.Formatter().formatException(sys.exc_info())

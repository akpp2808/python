# -*- coding: utf-8 -*-
"""
Created on Jul 31, 2013
filedesc:
@author: serg
"""
import re

txt = 'EUR   0'


print re.search('EUR\s*(\d+)', txt).group(1)


# -*- coding: utf-8 -*-

def is_ascii(s):
    return all(ord(c) < 128 for c in s)


print  is_ascii('dfcz в')
print u'вася'

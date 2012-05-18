#!/usr/bin/python
# -*- coding: utf-8 -*-


#s = 'тест'
#print s


print unicode('\xc3\xa4\xc3\xb6\xc3\xbc', 'utf-8')
print u'\u0442\u0435\u0441\u0442'.encode('utf-8')
print u'тест'.decode('utf-8')


help(unicode())
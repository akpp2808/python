# -*- coding: utf-8 -*-
"""
Created on Jun 8, 2013
filedesc:
@author: serg

"""
import re


html = '<b>You: </b> hello 1232'  # get text: 'hello 1232'
#html = 'Guest_16'

#print re.search('[^\<\>]+', html).group()
#print re.search('<[\/\!]*?[^<>]*?>', html).group()
#print re.search('<.*?./.*?>', html).group()

pattern = '<.*?./.*?>'
#print html.replace(pattern, '')


# поиск с инверсией
# не включая в найденное
# все кроме слова
# Регулярное выражение, исключить слово или строку
#html = 'bla hello bla1 bla bhello2'


#print re.search('(?<=bla)?+', html).group(0)
#print re.search('(?<=abc)def', 'abcdef').group(0)
#print re.search('(?<=-)\w+', 'spam-egg').group()
#print re.search('^(?!foo)+', 'foobar').group()
#print re.search('<[\/\!]*?[^<>]*?>', html).group(0)

#print re.search('<[\/\!]*?[^<>]*?>(.*)<[\/\!]*?[^<>]*?>(.*)', html).group(2)
print re.sub('<[\/\!]*?[^<>]*?>', '_', html)  # _You: _ hello 1232

print ' hello'.strip()

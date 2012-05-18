import re

str = 'Hi ss4@gmail.com!2'
str = 'Hi test@example.com!'

#print re.compile('Hi\s+([^!]+)').search(str).group(1) #24

#print re.compile('Hi\s+([^!]+)')


action = 'aaddAdmins'

if re.search('^add|^set', action):
    print action
#print r.group(0) if r else ''
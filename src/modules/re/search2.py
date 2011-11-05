import re

str = 'Hi ss4@gmail.com!2'
str = 'Hi test@example.com!'

print re.compile('Hi\s+([^!]+)').search(str).group(1) #24
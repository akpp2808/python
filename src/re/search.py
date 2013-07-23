import re

str = '&lt;div class="welcome-text"&gt;Hi Guest_24!&lt;/div&gt;'
str = 'Hi ss4@gmail.com!'

#print re.compile('Guest_(\d+)!').search(str).group(1) #24



#=============================================================
html = 'Guest_16'
print html
print re.search('Guest_(\d+)',html).group(1)



text = '(1)Michael'

print re.search('\((\d*)\)', text).group(1)
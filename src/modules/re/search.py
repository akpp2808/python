import re

str = '&lt;div class="welcome-text"&gt;Hi Guest_24!&lt;/div&gt;'
str = 'Hi ss4@gmail.com!'

print re.compile('Guest_(\d+)!').search(str).group(1) #24
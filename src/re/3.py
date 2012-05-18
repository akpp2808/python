html = '''<!doctype html>
<html>
<head>
<ti1tle>        operators success 
registration title
</title>
</head>
<body>
   

        
Operator header



        
<h1>Operator registration template !</h1>
Please click to activate account: <a href="http://192.168.154.113:8070/verification/70aba7de0726d87a14c933e85aa0ecb3/" target="_blank">http://192.168.154.113:8070/verification/70aba7de0726d87a14c933e85aa0ecb3/</a>



        
Base default footer


  
</body>
</html>
'''

import re
#print re.compile('\<title>(.*)').search(html).group(1)
r = re.search('\<title\>([^\<]*)',html,1) and ''
print r and r.group(1)


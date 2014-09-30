# -*- coding: utf-8 -*-
"""
Created on Jul 28, 2013
filedesc:
@author: serg
"""
import re

html = """
    </script>
    <!-- end of analytics identify section -->        <script type="text/javascript">
var API_SERVER_HOST = '192.168.0.120:8081',
WEB_SOCKET_SWF_LOCATION = 'http://192.168.0.120:8081/user/static/WebSocketMainInsecure.swf',
params = {
    sceneid:        'chathere',
    static_root:    'http://192.168.0.120:8081/user/static/games/chat/',
    gameID:         6,
    chatOnly:       true,
    ajaxOTT:        '/ru/ajax/ott/',
    one_time_token: '',
    api_url:        '192.168.0.120:8081',
    emailForFeedback: 'support@ezscratch.com',
    customUI:       true,
    is_tablet: false}
    </script>
    <script type="text/javascript" src="http://192.168.0.120:8081/user/static/js/ru/chat.min.js"></script>
    <div class="feedback">
        <a class="chat" href="javascript:void(0)" onclick="Chat.toggle('chatbox')">Поддержка</a>
    </div>
    <div id="chathere"></div>
</body>
</html>
"""

token_re = re.compile('one_time_token: *?[\'\"](.*?)[\'\"]')
# print re.search(ur'one_time_token+', html).group(0)
pattern = 'one_time_token[^\']()'
print token_re.search(html)
# print dir(re)







html = 'Guest_16'
print html
print re.search('Guest_(\d+)',html).group(1)



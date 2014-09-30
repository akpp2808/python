# -*- coding: utf-8 -*-
"""
Created on Dec 16, 2013
filedesc:
@author: serg
"""
# token_re = re.compile('one_time_token: *?"(.*?)",')

# if target.is_registered() and field in required_user_fields and not validator(value):
# guest
import re

# print 0 or 1 and not 0
# print 1 or 1 and not 0


str = """Traceback (most recent call last):
  File "/var/www/jenkins/workspace/905PREMERGEwithdrawals/GameServer/venv/local/lib/python2.7/site-packages/gevent/pywsgi.py", line 438, in handle_one_response
    self.run_application()
  File "/var/www/jenkins/workspace/905PREMERGEwithdrawals/GameServer/venv/local/lib/python2.7/site-packages/gevent/pywsgi.py", line 425, in run_application
    self.process_result()
  File "/var/www/jenkins/workspace/905PREMERGEwithdrawals/GameServer/venv/local/lib/python2.7/site-packages/gevent/pywsgi.py", line 416, in process_result
    self.write(data)
  File "/var/www/jenkins/workspace/905PREMERGEwithdrawals/GameServer/venv/local/lib/python2.7/site-packages/gevent/pywsgi.py", line 373, in write
    self.socket.sendall(msg)
  File "/var/www/jenkins/workspace/905PREMERGEwithdrawals/GameServer/venv/local/lib/python2.7/site-packages/gevent/socket.py", line 509, in sendall
    data_sent += self.send(_get_memory(data, data_sent), flags)
  File "/var/www/jenkins/workspace/905PREMERGEwithdrawals/GameServer/venv/local/lib/python2.7/site-packages/gevent/socket.py", line 483, in send
    return sock.send(data, flags)
error: [Errno 32] Broken pipe
<ApiSocketServer fileno=4 address=127.141.210.137:8081>: Failed to handle request:
  request = GET /dev/clients/bonus_rounds/seamermaid/images/100/en/tail1.png HTTP/1.1 from ('127.0.0.1', 42491)
  application = <function noodlesapp at 0x715ff50>

 """
pywsgi_err = '(.*?): Failed to handle request:\n  request = (.*?) from (.*?)\n  application = (.*?)\n\n'
# print re.search('(.*?): Failed to handle request:\n  request = (.*?) from (.*?)\n  application = (.*?)\n\n', str)
# print re.search(pywsgi_err, str)
# print  'error: [Errno 32] Broken pipe' in str
# print '%s: Failed to handle request:\n  request = %s from %s\n  application = %s\n\n' in str
# print '%s: Failed to handle request:\n  request = %s from %s\n  application = %s' in str


class HashWrap(object):
    def __init__(self, **kwargs):
        self._data = kwargs

    def data(self):
        return self._data

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self._data == other._data)

    def __ne__(self, other):
        return not self.__eq__(other)


h = HashWrap(**{'a':1})
print 'h', h, h.data()


# import time
# 
# 
# while True:
#     try:
#         1 / 4
#         print 'success'
#         break
#     except:
#         print 'e',
#         time.sleep(1)

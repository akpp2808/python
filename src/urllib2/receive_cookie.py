# -*- coding: utf-8 -*-
"""
Created on Jul 10, 2013
filedesc: Retrieving Cookies in python
@author: serg

"""
import cookielib
import urllib2
import re

uri = 'http://192.168.0.110:8077'

#cookies = cookielib.LWPCookieJar()
cookies = cookielib.CookieJar()
handlers = [
    urllib2.HTTPHandler(),  # http_handler
    urllib2.HTTPSHandler(),  # https_handler
    urllib2.HTTPCookieProcessor(cookies)  # cookie_handler
    ]
opener = urllib2.build_opener(*handlers)
opener.addheaders = [
    ('User-Agent', 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)'),
    ]


req = urllib2.Request(uri)
result = opener.open(req)
html = result.read()
print 'req', req, dir(req)
print 'result', result, dir(result)
print 'html', html


#print 'cookies', cookies
#print 'cookies', cookies._cookies
#
#print 'cookies', dir(cookies)
#for cookie in cookies:
#    print cookie.name, cookie.value

#get_cookie = lambda name: cookie for cookie in cookies:


def get_cookie(name):
    for cookie in cookies:
        if cookie.name == 'gusid':
            val = cookie.value
    assert val
    return val


def get_guest_id(html):
    match = re.search('Guest_([\d\w]+)', html)
    return match and match.group(1) or None

print 'session_id', get_cookie('gusid')
print 'user_id', get_guest_id(html)

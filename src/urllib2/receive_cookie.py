# -*- coding: utf-8 -*-
"""
Created on Jul 10, 2013
filedesc: Retrieving Cookies in python
@author: serg
http://stackoverflow.com/questions/4582964/python-urllib2-cookielib
http://stackoverflow.com/questions/5606083/how-to-set-and-retrieve-cookie-in-http-header-in-python
http://stackoverflow.com/questions/525773/accept-cookies-in-python
"""
import cookielib
import urllib2
import re

url = 'http://127.0.0.1:8077'


class CookieHelper():
    def __init__(self):
        self.cookies = cookielib.CookieJar()
        handlers = [
            urllib2.HTTPHandler(),  # http_handler
            urllib2.HTTPSHandler(),  # https_handler
            urllib2.HTTPCookieProcessor(self.cookies)  # cookie_handler
            ]
        self.opener = urllib2.build_opener(*handlers)
        self.opener.addheaders = [
        ('User-Agent', 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)'),
#         ('Cookie', 'usid=745bd13e22f4596b11e5e9c23d9c37ff'),
            ]

    def open(self, uri):
        req = urllib2.Request(uri)
        result = self.opener.open(req)
        self.html = result.read()
        return self.html

    def get_cookie(self, name):
        for cookie in self.cookies:
            if cookie.name == name:
                val = cookie.value
#         assert val
        return val

    def get_guest_id(self):
        match = re.search('Guest_([\d\w]+)', self.html)
        return match and match.group(1) or None

handler = CookieHelper()
handler.open(url)
print 'user_id', handler.get_guest_id()
print 'cookie', handler.get_cookie('gusid')


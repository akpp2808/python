#coding: utf-8
from urlparse import urlparse
class LazyUrl:
    parsed_url = None
    def __init__(self, url):
        print 'init'
        self.url = url
 
    def __parse_url(self):
        print 'only one calculation'
        #print self.url
        self.parsed_url = urlparse(self.url)
        print self.parsed_url
        return self.parsed_url
 
    def __get_parsed_url(self):
        return self.parsed_url or self.__parse_url()
 
    def __getattr__(self, *args, **kwargs):
        url_attr = args[0]
        return getattr(self.__get_parsed_url(), url_attr)
 
lazy = LazyUrl('http://ya.ru/test/?test=test&var=2')
#Вычисление производится только при первом обращении к объекту
print lazy.scheme, lazy.netloc, lazy.path, lazy.query, lazy.params, lazy.kk
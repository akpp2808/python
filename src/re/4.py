#<input name="fileIDs" value="123456" />
#Code snippet:

#from 3 import 
import urllib, urllib2
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self, fh):
        """
        {fh} must be an input stream returned by open() or urllib2.urlopen()
        """
        HTMLParser.__init__(self)
        self.fileids = []
        self.feed(fh.read())
    def handle_starttag(self, tag, attrs):
        if tag == 'input':
            attrD = dict(attrs)
            if attrD['name'] == 'fileIDs':
                self.fileids.append(attrD['value'])
    def get_fileids(self):
        return self.fileids
    
opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open("http://www.example.com/200.html")
myparser = MyHTMLParser(response)
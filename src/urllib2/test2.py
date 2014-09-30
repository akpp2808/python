# -*- coding: utf-8 -*-
"""
Created on Jan 2, 2014
filedesc:
@author: serg
"""
import urllib2


def url_opener(url, zone, login, password):
    handler = urllib2.HTTPDigestAuthHandler()
    handler.add_password(zone, url, login, password)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    return urllib2.urlopen(url)

# url = get_config('LOTTERY_URL') + 'scratch/paytable/%s' % cur_id


fp = url_opener('http://ls.ezd.lan/scratch/paytable/2',
                'LSAPI', 'LotteryGameAPI', 123)
print 'fp.read()', fp.read()
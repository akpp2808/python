# -*- coding: utf-8 -*-
"""
Created on Jul 25, 2013
filedesc:
@author: serg
"""

# import datetime
from datetime import datetime, timedelta
import time

from test_model import AccessToken
ONE_TIME_TOKEN_TTL = 172800
TTL = timedelta(seconds=60)

now = datetime.now
[m.delete() for m in AccessToken.objects.all()]
print 'all', len(AccessToken.objects.all())
def delete_expired_models():
    d = now() - TTL
    d = now()
    print 'need time', d
    
#     for p in AccessToken.objects.zfilter(created_on__lt=datetime(2010, 1, 30)):
#     d = datetime(2010, 4, 20, 5, 2, 0)
    print 'filtered', len(AccessToken.objects.zfilter(created_on__lt=d))
    for m in AccessToken.objects.zfilter(created_on__lt=d):
        print 'id:', m.id, m.created_on
#     for model in AccessToken.objects.all():
#         lifetime = now - model.created_on
#         expired_on = model.created_on + TTL
#         print 'expired_on', expired_on
#         print 'lifetime', lifetime
#         if lifetime > datetime.timedelta(seconds=60):
#             #delete
#             pass

def get_all(each=False):
    print 'get all', len(AccessToken.objects.all())
    if each:
        for m in AccessToken.objects.all():
            print m.id, m.created_on

def create_new():
    #create
    p = AccessToken(
                    session_id='1',
                    operator_id='1',
                    )
    p.save()

def get_filtered():
    d = now()
    print d
    for m in AccessToken.objects.zfilter(created_on__lt=now()):
        print 'id:', m.id, m.created_on


create_new()
time.sleep(1)
get_all(1)
get_filtered()

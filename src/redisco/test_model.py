# -*- coding: utf-8 -*-
"""
Created on Jul 24, 2013
filedesc:
@author: serg
http://www.timmedina.net/post/642641575/introducing-redisco-python-containers-and-simple
"""

from redisco import models
from redisco.models.base import Mutex
import unittest
import redisco
import time
class AccessToken(models.Model):
#     name = models.Attribute(required=True)
#     fave_colors = models.ListField(str)
#     created_on = models.DateField(auto_now_add=True)
#     updated_on = models.DateField(auto_now=True)
    
    session_id = models.Attribute(required=True)
    url = models.Attribute()  # default None
    ref_url = models.Attribute()  # default None
#     operator_id = models.Attribute(required=True)  # для авторизации ws
    used = models.BooleanField(default=False)
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    

    #что кто думает про этот метод, нужен ли он?
    @classmethod
    def get(cls, id):
        return cls.objects.get_by_id(id)
    
    
def test_delete_all():
    print 'delete all'
    [m.delete() for m in AccessToken.objects.all()] 
#     AccessToken.objects.create(session_id=1)
    
# #     AccessToken.objects.create(first_name="Clark", last_name="Kent")
# #     AccessToken.objects.create(first_name="Granny", last_name="Mommy")
# #     AccessToken.objects.create(first_name="Granny", last_name="Kent")
# 
# #     for person in AccessToken.objects.all():
# #         person.delete()
#     
#     print 'all', len(AccessToken.objects.all())
#     self.assertEqual(0, self.client.scard('Person:all'))
    

def test_get_all():
    print 'get all', len(AccessToken.objects.all())
#     for m in AccessToken.objects.all():
#         print m

def test_create_and_delete():
    #create
    p = AccessToken(
                    session_id='1',
                    operator_id='1',
                    )
    p.save()
    print 'create', p
    id = p.id
    p = AccessToken.get(id)
    p.delete()
    p = AccessToken.get(id)
    print 'deleted', p
    
def test_delete():
    p = AccessToken.get(79)
    p.delete()
    
#     print p
# test_create()
# test_delete_all()
# test_get_all()
# test_delete()
# test_get_all()
from datetime import datetime, timedelta

class TestModel(unittest.TestCase):
    
    def setUp(self):
        self.client = redisco.get_client()
#         self.client.flushdb()

    def tearDown(self):
        pass
#         self.client.flushdb()

    def test_filter_date(self):
        from datetime import datetime

        class Post(models.Model):
            name = models.CharField()
            date = models.DateTimeField()

        now = datetime.now
        dates = (
            datetime(2009, 12, 21, 1, 40, 0),
            datetime(2010, 1, 10, 1, 40, 0),
            datetime(2010, 1, 20, 1, 40, 0),
            datetime(2010, 1, 26, 1, 40, 0),
            datetime(2010, 1, 30, 1, 40, 0),
            datetime(2010, 2, 20, 1, 40, 0),
            datetime(2010, 5, 20, 1, 40, 0),
        )

        i = 0
#         for date in dates:
# #             Post.objects.create(name="Post#%d" % i, date=date)
# #             i += 1
#             p = Post(name="Post#%d" % i, date=now())
#             p.save()
#             time.sleep(1)

#         self.assertEqual([Post.objects.get_by_id(4)],
#                 list(Post.objects.filter(date=
#                     datetime(2009, 12, 21, 1, 40, 0))))
# 
#         lt = (0, 2, 3, 4)
#         res = [Post.objects.get_by_id(l + 1) for l in lt]
#         print 'res', len(set(res))
#         print 'res', res
#         self.assertEqual(set(res),
#                 set(Post.objects.zfilter(
#                     date__lt=datetime(2010, 1, 30))))
#         for p in Post.objects.all():
#             print p
#         for p in Post.objects.zfilter(date__gte=datetime(2010, 1, 30, 1, 40, 0)):
        now = datetime.now()
#         for p in Post.objects.zfilter(date__lt=now):
        for p in Post.objects.zfilter(date__gt=datetime(2013, 7, 25, 17, 2, 11, 0)):
            print p
#         print Post.objects.get_by_id(7)
        
        
if __name__ == '__main__':
    unittest.main()
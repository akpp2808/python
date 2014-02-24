# -*- coding: utf-8 -*-
"""
Created on Feb 16, 2014
filedesc:
@author: serg
"""

from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')


@app.task
def hello():
    return 'hello world'

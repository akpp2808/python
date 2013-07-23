# -*- coding: utf-8 -*-

import uuid
import json
import time
import random
import logging
import traceback
from ctypes import c_int
from itertools import ifilter as flt
from websocket import create_connection
from multiprocessing import Pool, Value, Queue, Process
import unittest


class TestProceess(unittest.TestCase):
    def test_main(self):
        from multiprocessing import Pool


def f(x):
    print 2
    return x*x



p = Pool(5)
p.map(f, [1,2,3])

#if __name__ == '__main__':
#    unittest.main()

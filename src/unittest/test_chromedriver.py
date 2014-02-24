# -*- coding: utf-8 -*-
"""
Created on Jan 12, 2014
filedesc:
@author: serg
"""



import unittest
import time

from functools import wraps
import errno
import os
import signal
import time
import xmlrunner
import sys
from noodles.utils.webdriver import wd_instance
from tests.test_locators import MAX_TIME_WAITING


def get_balance(driver, selector='.b-balance_11_info'):
    i = 0
    element = driver.find_element_by_css_selector(selector)
    balance = element.text

    while not balance:
        time.sleep(1)
        balance = driver.find_element_by_css_selector(selector).text
        if i > MAX_TIME_WAITING:
            break
        i += 1
    return balance


class Test(unittest.TestCase):
    def setUp(self):
        self.inc = 0
        pass
#         self.driver = wd_instance('chrome')
#         self.driver.implicitly_wait(30)

    def test_main(self):
        while True:
#             self.driver.get('http://test_admin1:testtest@gs.983.jnode7.ezd.lan/dev/clients/searover/index.html')
#             try:
                self.driver = wd_instance('chrome')
                self.driver.get('http://test_admin1:testtest@127.0.0.1:8081/dev/clients/searover/index.html')
                print 'balance:', time.time(), [get_balance(self.driver)], self.inc
#             except Exception, e:
#                 print 'err', e
#             finally:
#                 self.inc += 1
#                 self.driver.quit()

if __name__ == '__main__':
    unittest.main()

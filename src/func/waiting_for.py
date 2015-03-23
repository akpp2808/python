# -*- coding: utf-8 -*-
"""
Created on Feb 16, 2015
filedesc:
@author: serg
"""

import time

default = -1
timeout = 3


def waiting_for_celery(fn, timeout=timeout, attr=default, eq=default):
    """
    1 fn() result
    1.1 fn() == eq
    2 fn().attr result
    2.1 fn().attr result == eq
    """
    i = 0
    timeout = 5
    _tmp_result = default
    while True:
        result = fn()
        # 1 fn() result
        if eq == default and attr == default:
            _tmp_result = result
            return _tmp_result
        # 2.1 fn().attr result == eq
        elif eq != default and attr != default:
            _tmp_result = getattr(result, attr, None) == eq
            return _tmp_result
        # 2 fn().attr result
        elif attr != default:
            _tmp_result = getattr(result, attr, None)
            return _tmp_result
        # 1.1 fn() == eq
        elif eq != default:
            _tmp_result = result == eq
            return _tmp_result
        elif i > timeout:
            return _tmp_result
        else:
            time.sleep(1)
            i += 1


#         sa_session.expire_all()
#         result = fn()
#         print 'result', result, i
# 
#         if result is not None and eq is not None\
#                 and result == eq:
#             print '1'
#             return result
# #         elif result is not None and attr is None:
# #             print '2'
# #             return result
#         elif result is not None and attr is not None\
#                 and getattr(result, attr, None):
#             print '3'
#             return result
#         elif i > timeout:
#             print '4'
#             return result
#         else:
#             print '5'
#             time.sleep(0.2)
#             i += 1


waiting_for_celery(lambda: None, eq=11)

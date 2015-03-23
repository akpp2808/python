# -*- coding: utf-8 -*-
"""
Created on Sep 30, 2014
filedesc:
@author: sergey.g

DataError: (DataError) (1264, "Out of range value for column 'money' at row 1") 'INSERT INTO transactions (action_id, game_instance_id, currency_id, money, wagering_req, wagering_req_balance, bonus_money, t_type, sub_type, external_id, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' ('ed5a64dacede44f3a6b5c48627daee4c', None, 4, 4294967295L, 8589934590L, 8589934590L, 4294967295L, 'BonusTransaction', None, None, None)
"""

from datetime import datetime

from create_engine import Transaction, sa_session
from sqlalchemy.sql.functions import func
from sqlalchemy import select
import unittest


from sqlalchemy import alias
def add(money):
    tr = Transaction(money=money)
    print 'tr.created_at0', tr.created_at
    sa_session.add(tr)
    print 'tr.created_at1', tr.created_at
    sa_session.commit()
    print 'tr.created_at2', tr.id, tr.created_at
#     tr.created_at = datetime(2014, 10, 20, 6, 39, 24, 12345)
# #     tr.created_at = datetime(2014, 10, 20, 6, 39, 24, 0123)
# #     sa_session.flush()
# #     commit_time = tr.created_at
#     print 'tr.created_at1', tr.created_at
# #     assert init_time == commit_time, (init_time, commit_time)
# #     sa_session.commit()
# 
#     t = sa_session.query(Transaction).get(1)
#     print 't.created_at2', t.created_at
#     tr2 = Transaction(money=t.money, balance=t.balance, created_at=t.created_at)
#     sa_session.add(tr2)
# 
#     print 't.created_at3', t.created_at
#     sa_session.commit()
#     print 't.created_at4', t.created_at


class TestInsert(unittest.TestCase):
    def test_main(self):
        for i in range(1):
            add(1)

if __name__ == '__main__':
    unittest.main()

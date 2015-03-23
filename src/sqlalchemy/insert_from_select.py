# -*- coding: utf-8 -*-
"""
Created on Sep 30, 2014
filedesc:
@author: sergey.g

DataError: (DataError) (1264, "Out of range value for column 'money' at row 1") 'INSERT INTO transactions (action_id, game_instance_id, currency_id, money, wagering_req, wagering_req_balance, bonus_money, t_type, sub_type, external_id, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' ('ed5a64dacede44f3a6b5c48627daee4c', None, 4, 4294967295L, 8589934590L, 8589934590L, 4294967295L, 'BonusTransaction', None, None, None)
"""


# from create_engine_inheritance import Transaction, sa_session
from create_engine import Transaction, sa_session
from sqlalchemy.sql.functions import func
from sqlalchemy import select
import unittest

# tr = Transaction(money=200)
# tr.balance = func.coalesce(Transaction.balance, 0) + 1
# tr.balance = select([select([Transaction.money]).alias('tmp')])
# tr.balance = select([select([Transaction.money]).alias('tmp')])

# sql = select([select([func.sum(Transaction.money)]).alias('tmp')])
# sql = select([select([func.sum(Transaction.money)]).alias('tmp')])
# sql = select([func.sum(select([Transaction.money]).as_scalar())])
# tr.balance = sql
# print 'sql', sql
# 
# sa_session.add(tr)
# sa_session.commit()
# 
# print 'tr', tr

from multiprocessing import Pool
from sqlalchemy.orm.util import aliased
p = Pool(5)


# def f(x):
#     sql = select([select([func.sum(Transaction.money)]).alias('tmp')])
#     tr.balance = sql
#     sa_session.add(tr)
#     sa_session.commit()
#     return 1

#10 000
#1. money :13.222
#2. money & balance select select: 65.0, 71

#10 000
#raw insert
#money  6.118s
#m+b = 50.549s | 18.998s, 19.003s, 19.950s, 20.184s, 21.008s
#m+b+index = 90.890s
#m+b+select select = 49.944s, 127.115s | 1.091s, 2.012s, 2.945s



connection = sa_session.connection()
def raw_insert(money):
#     print 'money', money
#     connection.execute('select 1;').scalar()
#     connection.execute('insert into transactions (money) values (%s)' % money)
#     connection.execute('insert into transactions (money, balance) select %s, sum(money)+%s from transactions t;' % (money, money))
#     connection.execute('insert into transactions (money, balance) select %s, sum(money) from transactions;' % money)
# insert into transactions (money, balance) values (1, (select sum(money) from transactions t));
#     connection.execute('insert into transactions (money, balance) values (%s, (select sum(money) from (select money from transactions) tmp));' % money)
    connection.execute('BEGIN')
#     set @prev = (select balance from transactions order by created_at desc limit 1);
    connection.execute('''
    insert into transactions (money, balance) values (
        %s,
        (select ifnull((select balance from transactions t order by created_at desc limit 1), 0) + %s)
    );
    ''' % (money, money)
    )
#     insert into transactions (money, balance) values (1, 1);
#      % (money)
    connection.execute('COMMIT')

from sqlalchemy import alias
def add(money):
#     sql = select([select([func.coalesce(func.sum(Transaction.money), 0) + money]).alias('tmp')])
#     sql = select([func.sum(Transaction.money).label('g')])

    Tr = aliased(Transaction, name='tr')
    sql = select([func.coalesce(func.sum(Tr.balance), 0) + money])
#     sql = sa_session.query(func.sum(Transaction.money))
#     .as_scalar()
#     .label('aa')
#     print dir(sql)
#     print 'sql', sql
    tr = Transaction(money=money)
    tr.balance = sql
    print 'tr.created_at0', tr.created_at
#     tr.moeny = 4294967295
#     tr.balance = -1
    sa_session.add(tr)
    print 'tr.created_at1', tr.created_at
    sa_session.commit()
    print 'tr.created_at2', tr.created_at


class TestInsert(unittest.TestCase):
    def test_main(self):
        for i in range(1):
#             add(4294967295)
            add(1)
#             raw_insert(1)



if __name__ == '__main__':
    unittest.main()
#     for i in range(1000):
#         add(1)
#     print 'finish'
    

#     pool = Pool(processes=4)              # start 4 worker processes
#     result = pool.apply_async(add, range(1000))    # evaluate "f(10)" asynchronously
#     print dir(result)

#     print result.get(timeout=1)           # prints "100" unless your computer is *very* slow
#     print pool.map(add, range(1000))          # prints "[0, 1, 4,..., 81]"

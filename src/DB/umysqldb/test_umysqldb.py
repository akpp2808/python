# -*- coding: utf-8 -*-
"""
Created on Oct 19, 2014
filedesc:
@author: sergey.g
"""

import umysqldb
umysqldb.install_as_MySQLdb()
import MySQLdb
MySQLdb is umysqldb
True
conn = MySQLdb.connect(host='localhost', db='test')
curs = conn.cursor()
# curs.execute("INSERT INTO test.transactions (money, balance, created_at) VALUES (1, 1, datetime.datetime(2014, 10, 20, 6, 39, 24, 123456)")
curs.execute("INSERT INTO transactions (money, created_at) VALUES (1, '2011-08-21 14:11:09.123456')")
curs.execute("COMMIT")
curs.execute("select * from transactions")
print curs.fetchall()
conn.close()

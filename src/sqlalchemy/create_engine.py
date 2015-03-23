# -*- coding: utf-8 -*-
"""
Created on Oct 2, 2014
filedesc:
@author: sergey.g
dbms - Database management systems
dsn - Data source name

SQLAlchemy will not actually create the database for you.
You have to connect to an existing database. It will then create all the tables

"""

import datetime
from sqlalchemy import create_engine, Column, Integer, text, func, String,\
    DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql.base import TIMESTAMP, INTEGER, DATETIME

import umysqldb
import uuid
print 'umysqldb', umysqldb
umysqldb.install_as_MySQLdb()

DATABASE = dict(host='localhost',
                dbms='mysql',
                dbname='test',
                username='root',
                password='')

#mysql://root:@localhost/account?charset=utf8
dsn = '%(dbms)s://%(username)s:%(password)s@%(host)s/%(dbname)s?charset=utf8'\
    % DATABASE
engine = create_engine(dsn, echo=1)

#create table
Base = declarative_base()


class Transaction(Base):
    __tablename__ = 'transactions'
#     id = Column(Integer, primary_key=True)
#     id = Column(String(32), primary_key=True, default=uuid.uuid4().hex)
    id = Column(String(32), primary_key=True, default=lambda: uuid.uuid4().hex)
    #CREATE INDEX ix_transactions_currency_id ON transactions (currency_id)
#     currency_id = Column(Integer, index=True)
    currency_id = Column(Integer, index=True)
    money = Column(Integer, nullable=False)
#     balance = Column(INTEGER(unsigned=True), nullable=False)
#     created_at = Column(DATETIME(fsp=6),
#                         server_default=text('CURRENT_TIMESTAMP(6)'),
#                         onupdate=func.now(),
#                         nullable=False)
#     created_at = Column(TIMESTAMP(fsp=6),
#                         server_default=text('CURRENT_TIMESTAMP(6)'),
#                         nullable=False)
#     created_at = Column(DATETIME(),
#                         server_default=text('CURRENT_TIMESTAMP'),
#                         onupdate=func.now(),
#                         nullable=False)
    created_at = Column(TIMESTAMP(fsp=6),
                        nullable=False,
                        default=datetime.datetime.now())

    def __repr__(self):
        return '<Transaction(id: {0.id},'\
            'money: {0.money}, balance: {0.balance})>'.format(self)

metadata = Base.metadata
metadata.drop_all(engine)
metadata.create_all(engine)


#Создание сессии
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

sa_session = Session()
print 'finish'

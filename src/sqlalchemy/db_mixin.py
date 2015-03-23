# -*- coding: utf-8 -*-
"""
Created on Mar 15, 2015
filedesc:
@author: serg
"""


import datetime
from sqlalchemy import create_engine, Column, Integer, text, func, String,\
    DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, declared_attr,\
    has_inherited_table
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

dsn = '%(dbms)s://%(username)s:%(password)s@%(host)s/%(dbname)s?charset=utf8'\
    % DATABASE
engine = create_engine(dsn, echo=0)

#create table
Base = declarative_base()
Base2 = declarative_base()


class Action(Base):
    __tablename__ = 'actions'
    __mapper_args__ = {'polymorphic_on': 'type'}
    id = Column(Integer, primary_key=True)
    type = Column(String(32), nullable=False)

class BaseFields():
#     operator_id = Column(Integer, ForeignKey('operators.id'))

    @declared_attr
    def operator_id(cls):
#         print 'HERE', cls.__mro__[1:]
#         print 'HERE', Action in cls.mro()
#         print 'HERE', ShardBase in cls.mro()

#         is_shard_table = ShardBase in cls.mro()
        is_shard_table = Action in cls.mro()

        if not is_shard_table:
#             print '1'
            return Column(Integer)
        else:
#             print '2'
            return Column(Integer, ForeignKey('operators.id'))


class BonusDef(Base, BaseFields):
    __tablename__ = 'bonuses'
    __mapper_args__ = {'polymorphic_identity': 'Transaction'}
    id = Column(String(32), primary_key=True, default=lambda: uuid.uuid4().hex)



class BonusDist(Action, BaseFields):
    __tablename__ = 'bonuses_dist'
    action_id = Column(Integer, ForeignKey('actions.id'), primary_key=True)


# print 'bonus_def', dir(BonusDef)
# print 'has_inherited_table(Base)', has_inherited_table(Base)


# print 'mro', BonusDist.mro()

# metadata = Base.metadata
# metadata.drop_all(engine)
# metadata.create_all(engine)


#Создание сессии
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

sa_session = Session()
print 'finish'


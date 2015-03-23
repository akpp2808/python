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
from sqlalchemy import create_engine, Column, Integer, text, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql.base import TIMESTAMP, INTEGER, DATETIME




import umysqldb
from sqlalchemy.schema import ForeignKey
from sqlalchemy.types import String

from importlib import import_module
umysqldb.install_as_MySQLdb()

DATABASE = dict(host='localhost',
                dbms='mysql',
                dbname='test',
                username='root',
                password='')

#mysql://root:@localhost/account?charset=utf8
dsn = '%(dbms)s://%(username)s:%(password)s@%(host)s/%(dbname)s?charset=utf8'\
    % DATABASE
engine = create_engine(dsn, echo=0)

#create table
# Base = declarative_base()

#Создание сессии
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
sa_session = Session()


def get_fixtures_class(clz, fixtures_path='fixtures'):
    if getattr(clz, '_fixtures_class', None) is None:
        return None
    assert isinstance(clz._fixtures_class, basestring), \
        '_fixtures_class should be a string for {}'.format(str(clz))
    fixtures = import_module(fixtures_path)
    fixtures_class = getattr(fixtures, clz._fixtures_class, None)
    if fixtures_class is None:
        raise Exception(
            "{0}.__init__ doesn't contain {1}!".format(
                fixtures_path, clz._fixtures_class))
    return fixtures_class


class AugmentingBase(object):
    _fixtures_class = None
    sa_session = sa_session

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'extend_existing': True,
    }

    @classmethod
    def load_fixtures(cls, session=sa_session):
        """
        Adds data that have been identified in the fixture into the database.
        @return: Fixture object if data successfully loaded,
                 Exception if error.
        """
        fixtures_class = get_fixtures_class(cls)
        if fixtures_class is None:
            return
        fixture = fixtures_class(cls, session)
        fixture.load()


Base = declarative_base(cls=AugmentingBase)


class Action(Base):
    __tablename__ = 'actions'
    __mapper_args__ = {'polymorphic_on': 'type'}
    id = Column(Integer, primary_key=True)
    type = Column(String(32), nullable=False)
    created_at = Column(
                        DATETIME(fsp=6),
#                         DATETIME(),
                        server_default=text('CURRENT_TIMESTAMP(6)'),
#                         server_default=func.now(6),
                        onupdate=func.now(),
                        nullable=False)


class Transaction(Action):
    __tablename__ = 'transactions'
    __mapper_args__ = {'polymorphic_identity': 'Transaction'}
    _fixtures_class = 'TestTransactionData'
    action_id = Column(Integer, ForeignKey('actions.id'), primary_key=True)
    money = Column(Integer, nullable=False)
    balance = Column(INTEGER(unsigned=True), nullable=False)
    created_at = Column(TIMESTAMP(fsp=6),
                        server_default=text('CURRENT_TIMESTAMP(6)'),
                        nullable=False)

    def __repr__(self):
        return '<Transaction(id: {0.id},'\
            'money: {0.money}, balance: {0.balance})>'.format(self)

metadata = Base.metadata
metadata.drop_all(engine)
metadata.create_all(engine)


Transaction.load_fixtures()

print 'finish'

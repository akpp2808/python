# -*- coding: utf-8 -*-
"""
Created on Jun 23, 2013
filedesc:
@author: serg

"""


import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String
from sqlalchemy.schema import Column, MetaData
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker


#engine = create_engine('sqlite:///:memory:', echo=True)
#Base = declarative_base()

host = 'localhost'
dbms = 'mysql'
dbuser = 'root'
dbuserpasswd = ''
dbname = 'test_db'

#mysql -u root -e "CREATE DATABASE IF NOT EXISTS $DBNAME"

#mysql://root:@localhost/test_db
dbdescr = '%(dbms)s://%(dbuser)s:%(dbuserpasswd)s@%(host)s/%(dbname)s' % locals()
print dbdescr
engine = create_engine(dbdescr,
                           echo=False,  # show debug info in console
                           pool_recycle=7200  # control the maximum age of connection
                           )
#engine.execute('CREATE DATABASE IF NOT EXISTS %s' % dbname)
Session = sessionmaker(bind=engine)  # Session.configure(bind=engine)
session = Session()

Base = declarative_base()
metadata = Base.metadata
META = MetaData()  # ???


class Temp(Base):
    """
    Class for temporary table
    @param Base Declarative Base
    """
    __tablename__ = 'temporary'
    __table_args__ = {'prefixes': ['TEMPORARY']}

    id = Column(Integer, primary_key=True)
    name = Column(String(256))

    def test(self):
        print 'self', dir(self)


#class Country(Base):
#    __tablename__ = 'countries'
#    __table_args__ = {'prefixes': ['TEMPORARY']}

metadata.create_all(engine)
#metadata.drop_all(engine)
t = Temp(name='hello')
t2 = Temp(name='hello2')

session.add(t)
session.add(t2)
session.commit()

print dir(Temp)
#session.rollback()
print 't', t2.id

#print t, t.id



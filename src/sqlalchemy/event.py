import datetime

import sqlalchemy


from sqlalchemy import event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.schema import Column, MetaData
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import mapper


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


now = datetime.datetime.now


@event.listens_for(mapper, 'init')
def init(target, args, kwargs):
#    if not target.id:
#        session.add(target)
#        session.flush()
#        session.add(target)
#        session.flush([target])
    print 'init_event', target.id


def before_insert(mapper, connection, target):
    if not target.id:
        session.add(target)
        session.flush([target])
    print 'before_insert!!!!!!!!!!!!!', target.id



#?charset=utf
class Temp(Base):
    """
    Class for temporary table
    @param Base Declarative Base
    """
    __tablename__ = 'temporary'
    __table_args__ = {'prefixes': ['TEMPORARY']}

    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    created_at = Column(DateTime(), default=now)

    def __init__(self, *args, **kwargs):
        print 'init', self.id
        super(Temp, self).__init__(*args, **kwargs)


#class Country(Base):
#    __tablename__ = 'countries'
#    __table_args__ = {'prefixes': ['TEMPORARY']}


#event.listen(Temp, 'before_insert', before_insert)

metadata.create_all(engine)
#metadata.drop_all(engine)
t = Temp()

session.add(t)
session.commit()

print 't', t.id
print 't', dir(t.__table__.columns)
for i in t.__table__.columns:
    print i.primary_key, i.key
    print dir(i)
#    print i, getattr(t, i)

#print t, t.id


import datetime,time
#print  dir(datetime.datetime.now())
#print  type(datetime.datetime.now())
#print  datetime.datetime.now().microsecond



from datetime import timedelta
d = timedelta(microseconds=1100001)
print ' _', d.total_seconds()*1000
print d.seconds
print d.microseconds
#print dir(d)

f = 3.14
f*10

print time.time()
print time.time()*100
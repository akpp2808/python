import datetime,time
now = datetime.datetime.now
'''
1 day = 86400 seconds (60*60*24)
'''

one_day_ago = now()-datetime.timedelta(seconds=3600)
print one_day_ago                           #2012-01-06 06:36:24.596983
print time.mktime(one_day_ago.timetuple())  #1325849839.0
print datetime.datetime.utcnow()            #2012-01-06 06:36:24.596983


#print dir(datetime)
##print help(datetime.timedelta)
#
#
#print dir(datetime.timedelta(days=1))
#print datetime.timedelta(days=1).total_seconds()
#
#print int(datetime.datetime.now().strftime('%s'))
##print datetime.datetime.now())
#
#
#
#one_hour_ago = now()-datetime.timedelta(seconds=3600)
#print one_hour_ago.timetuple()
#print time.mktime(one_day_ago.timetuple())
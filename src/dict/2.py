d = {}
#print dir(d)


r = {'iteration': 2, 'result': 'win'}
#d.update(r)
d.update(d, **d)
print d



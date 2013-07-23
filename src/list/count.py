#-*- coding: utf-8 -*-
#l = [1,2,3,4,5]
#print dir(l)
#print len(l)
#print l[:4]

#Python count of items in a lists of dictionary
#подсчитать кольчество словарей в списке по ключу
items = [
     {'a': 1},
     {'a': 3},
     {'a': 3},
     {'b': 4},
     {'c': 5},
     ]

#print help(l.count)


#print sum(len(val) for val in dictionary.itervalues())


#print len([i for i in l if i.get('a')])
action = 'a'
print len([d for d in items if action in d])
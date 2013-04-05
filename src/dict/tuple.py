keys = ['b', 'c']

t = (
     ('a', 1),
     ('b', 2),
     ('c', 3),
     )

result = {}

#print [key for key, value in t]
#for item, v in t:
#    print item, v

#print t.get('a')

d = {'b': 2}

for key, value in t:
    print key, value
#    if key == 'a1'

a = {'display_name': value for key, value in t if key == 'a1' and key in t}
print 'a=', a
#a = (value for value in t)
print d.update(a)
print d


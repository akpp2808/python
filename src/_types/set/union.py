'''
Created on May 23, 2013

@author: serg
'''



base = set()
base.add('trash')

a = set()
b = set()
c = set()
d = set()

a.add('a')
b.add('b')
c.add('b')
d.add('d')

l = [a, b, c, d]

print base.union(*l)


#union = lambda l: 
#print union

#base = a | b | c | d

print 'base', base
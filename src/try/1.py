class A():
    pass

a = A()
try:
    a.a
except AttributeError:
    print 'AttributeError'
else:
    print 'else'
class B(object):
    pass

class A(object):
    def __init__(self):
        print '--inittialsation--'
        self._b = None
    @property
    def b(self):
        if not self._b:
            self._b = B()
        return self._b
    
a = A()
b1 = a.b
b2 = a.b
print b1 is b2

a2 = A()
b3 = a2.b
b4 = a2.b
print b3 is b4

print 'b1 is b3 - %s'%str(b1 is b4)
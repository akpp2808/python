class B():
    pass

class A():
    
    def __init__(self):
        print 'init'
        self.b = B()
        

    def __getattr__(self, *args, **kwargs):
        print "__getattr__"

    
a = A()
b1 = a.b
b2 = a.b
print b1 is b2

a1 = A()


print a1.b is b1

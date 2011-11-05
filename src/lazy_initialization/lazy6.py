class B(object):
    pass

class A(object):
    pass

class Lazy(object):
    instance = None
    def __init__(self,obj):
        self.obj = obj
        
    def initialisation(self):
        print 'initialisation'
        self.instance = self.obj()
        return self.instance
    
    def get_inst(self):
        return self.instance or self.initialisation()
        
    def __getattr__(self, *args, **kwargs):
        attr_name = args[0]
        try:
            value = getattr(self.instance, attr_name)
        except AttributeError as e:
            value = self.get_inst()
            setattr(self.obj, attr_name, value)
        
        return value

  
l = Lazy(B)
print l.b
print l.b
print l.c

l2 = Lazy(B)
print l2.a
print l2.b


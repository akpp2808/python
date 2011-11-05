class B(object):
    @property
    def b(self):
        return 'b'

class A(object):
    b = 'a'

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
        attr = args[0]
        print attr
        return getattr(self.get_inst(), attr)
  
l = Lazy(A)
print l.b
print l.b


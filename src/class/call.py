class A():
#    def __getattr__(self,param):
#        print param
#        return {}
    def b(self):
        print 'hello'
        print dir(self)
    def __getattribute__(self,name):
        print name

print dir(A)


a = A()
a.b()

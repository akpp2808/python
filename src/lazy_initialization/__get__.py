class B():
    pass

class A():
    
    def __get__(self, instance, owner):
        print '__get__'
        

a = A();
a.b 
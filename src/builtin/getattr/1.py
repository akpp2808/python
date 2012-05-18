class Test():
    a = 1

t = Test()
print getattr(t, 'a')
print getattr(t, 'a1', None)
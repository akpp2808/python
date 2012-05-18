def func():
    a = 1
    b = False
    print globals().get('func').__name__
    
    return a and b

def func2():
    print globals().get('func').__name__

print func2() #false
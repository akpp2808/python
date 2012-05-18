a1 = 1
b = 2


def func():
    print locals()
    print  locals().get('a') or 0
    
func()
def wrapper1(func, *args): # with star
    func(*args)


def func2(x, y, z):
    print x+y+z

wrapper1(func2, 1, 2, 3)

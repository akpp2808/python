def increase(func):
    def gen(a, b):
        a += 1
        return func(a, b)
    return gen


# @increase
def Sum(a, b):
    print 'a', a, 'b', b
    return a + b

Sum = increase(Sum)
print Sum(2,4)
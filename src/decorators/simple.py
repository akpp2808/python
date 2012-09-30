def increase(func):
    def gen(a, b):
        a += 1
        return func(a, b)
    return gen


#positiveSum = is_positive(positiveSum)
@increase
def Sum(a, b):
    print 'a', a, 'b', b
    return a + b

print Sum(2,4)
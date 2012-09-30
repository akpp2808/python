def first(func):
    def gen(a, b):
        print 'first decorator!'
        return func(a, b)
    return gen


def second(func):
    def gen(a, b):
        print 'second decorator!'
        return func(a, b)
    return gen


@first
@second
def Summ(a, b):
    """
    Summ = second(first(Summ))
        or
    Summ = first(Summ)
    Summ = second(Summ)

    @result:
        first decorator!
        second decorator!
        a 2 b 4
    """
    print 'a', a, 'b', b
    return a + b


#Summ = second(first(Summ))
#Summ = first(Summ)
#Summ = second(Summ)
Summ(2, 4)

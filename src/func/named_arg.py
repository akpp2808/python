#def test(a, b, c=4):
def test(a, b=2, c):
    print 'a', a
    print 'b', b
    print 'c', c

test(1, 3, 2)
#test(1, c=3, 2)
#test(2,b=3)
#SyntaxError: non-keyword arg after keyword arg

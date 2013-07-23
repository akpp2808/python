def test(*args):
    print 'args', args + (5,)


def test_ext(*args):
    print 'args', args
    
    
    
test(12,3)

#a = (1, 2, 3)
#b = a + (4, 5, 6)
#
#print b
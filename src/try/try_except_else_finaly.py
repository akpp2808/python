import socket
import errno
def a():    
    try:
#         raise socket.error(32, 'bal')
        print 123
        
#         return
        
#         a = 1 /0
        
        
    #    result = 1 / 1
    #     raise Exception('')
    #     assert 0, 'bla'
    except Exception as e:
        print 'e.errno',e.errno, e[0]
        if e[0] in (errno.EPIPE, errno.ECONNRESET):
            return
        print "Exception presend", e
    else:
        
        print "not exception"
    finally:
#         print 'a', a
        print "executing finally clause"
        
a()

# option two
#try:
#    result = 1 * 1
#except ZeroDivisionError:
#    print "division by zero!"
#else:
#    
#    print "result is", result
#finally:
#    print "executing finally clause"
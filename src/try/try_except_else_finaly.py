try:
#    result = 1 / 1
    raise Exception('')
except:
    print "Exception presend"
else:
    print "not exception"
finally:
    print "executing finally clause"

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
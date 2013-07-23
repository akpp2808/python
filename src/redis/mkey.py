def mkey(pubsub=False, *params, **kwargs):
    """
    return a key composed of the arguments passed, delimeted by colon.
    for usage with redis
    """
#    print type(params)
#    print dir(params)
    print 'params', params
    print 'params', kwargs
    if pubsub:
        params + (80,)
    print 'params', params
    return ":".join([str(rt) for rt in params])




#print mkey(1, 2)
print mkey(pubsub=1, 3)
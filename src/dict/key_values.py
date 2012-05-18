d = {"max": 100, "step": 10, "min": 1}

print d

#for key,value in d.iteritems():
#    print key,value 
values = [None,None,None]
import json
#for key, val in json.loads(d).iteritems():
for key, val in d.iteritems():
    if key == 'min':
        values[0] = val  
    elif key == 'max':
        values[1] = val  
    elif key == 'step':
        values[2] = val
print values
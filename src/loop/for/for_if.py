for i in [1, 2, 3]:
    if 3 not in [1, 2, 3]:
        continue
    print i




l = [1,2,3]
for i in (x for x in l if x !=2):
    print i
    
    
import re    
rooms = ['r:1', 'r:2', 'r:3',]

for i in (r for r in rooms if not re.search('2', r)):
    pass


redis_rooms = ['r:1', 'r:2', 'r:3',]
rooms = []

# for key in (i for i in redis_rooms j for j in rooms):
#     print 'key', key


for i in redis_rooms:
    for j in rooms:
        if not re.search(j, i):
            print 'res', i
            
            
            
import re
blah = "word word: monty py: thon"
answer = re.sub('monty','',blah)
print answer
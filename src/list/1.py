# list1 = [['e9801c5c6c94a67281bc665ddf529eb7', '3afcbd789367f5aa1760e88155ccc8a0'], ['3ff145678515a4529e567db4b57a12c6']]
# print dir(list1)

def add(fn):
    def wrapped():
        return fn() + 1
    return wrapped

def a():
    return 1

def b():
    return 2

l = [a, b]
ll = []


print dir(l)
print 'l', l
print 'ind', l.index(a)
print 'ind', 
# print 'pop', l[l.index(b)] = 
print 'l', l
# for f in l:
#     f = add(f)
#     ll.append(f)
# #     print f()
for f in l:
#     print f
    l[l.index(f)] = add(f)
#     f = add(f)
#     print f
#     f = add(f)
#     print f()
for f in l:
# #     f = add(f)
    print f()
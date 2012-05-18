a = {'id': 1, 'created_at': 8, 'name': 'a'}
b = {'id': 5, 'created_at': 1, 'name': 'b'}
c = {'id': 3, 'created_at': 6, 'name': 'c'}
d = {'id': 2, 'created_at': 5, 'name': 'a'}


def compare(x, y):
#    print x,y
#    return 1
    return x.get('created_at') - y.get('created_at')
    print x.get('created_at') < y.get('created_at'), x.get('created_at'), y.get('created_at')
    return x.get('name') < y.get('name')

dicts_list = [a, b, c, d]
#first.sort(cmp=compare, key=None, reverse=False)
dicts_list.sort(key=lambda a: a.get('name'))

print dicts_list


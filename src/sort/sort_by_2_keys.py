# -*- coding: utf-8 -*-
"""
    сортировка по двум ключам
"""
 
a = {'id': 1, 'created_at': 8, 'name': 'a'}
c = {'id': 3, 'created_at': 6, 'name': 'c'}
b = {'id': 5, 'created_at': 1, 'name': 'b'}
d = {'id': 2, 'created_at': 5, 'name': 'd'}
e = {'id': 1, 'created_at': 7, 'name': 'e'}
 
 
dicts_list = [a, b, c, d, e]
dicts_list.sort(key=lambda a: (a.get('id'), a.get('created_at')))
 
print dicts_list
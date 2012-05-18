# -*- coding: utf-8 -*-

string = 'привет'
print string
print string.decode('utf8')

a = "a\x81b"
print type(a),a
b = a.decode("utf-8", "replace")
print type(b),b



s = a
print s,type(s)
s = s.decode('utf-8','replace').encode()

print s,type(s)
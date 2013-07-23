'''
conversion float to string in python
http://pkolt.ru/pages/24/
'''
import math
string_val = 'abc'
float_val = math.pi #3.141592653589793115997963468544185161590576171875
print '%s_%f'%(string_val,float_val)          #abc_3.141235
print '%s_%s'%(string_val,str(float_val))     #abc_3.14159265359
print '%s_%s'%(string_val,repr(float_val))    #abc_3.141592653589793
print '%s_%s'%(string_val,repr(float_val))    #abc_3.141592653589793
print '%.48f'%(float_val)#3.141592653589793115997963468544185161590576171875

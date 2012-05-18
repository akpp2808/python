'''
Created on Dec 9, 2011

@author: serg
'''
import time 
t = time.strftime('%s')   #1323424141
s = '%.3f'%time.time()

print s.split('.')[0]+s.split('.')[1]


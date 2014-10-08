'''
Created on Apr 10, 2013

@author: serg
'''
from multiprocessing import Pool
import time

def f(x):
    res = x*x
    print x, res,  '%.6f' % time.time()
    return res

if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes
    result = pool.apply_async(f, range(10))    # evaluate "f(10)" asynchronously
#     print dir(result)

#     print result.get(timeout=1)           # prints "100" unless your computer is *very* slow
    print pool.map(f, range(10))          # prints "[0, 1, 4,..., 81]"
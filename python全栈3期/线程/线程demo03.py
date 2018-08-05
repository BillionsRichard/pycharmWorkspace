# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 线程demo03.py 
@time: 2018/5/24 8:36 
"""
from pprint import pprint as P
import threading
import time

def sum_n(n):
    tot = 0
    for i in range(1, n+1):
        tot += i
    P('sum=%s' % (tot))

def mul_n(n):
    mul = 1
    for i in range(1, n+1):
        mul *= i
    P('%s!=%s' %(n, mul))


if __name__ == '__main__':
    start = time.time()
    t1 = threading.Thread(target=sum_n, args=(100000,))
    t2 = threading.Thread(target=mul_n, args=(100000,))

    t1.start()
    t1.join()
    t2.start()

    t2.join()
    print('cost:%s' %(time.time() - start))
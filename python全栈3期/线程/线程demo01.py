# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 线程demo01.py 
@time: 2018/5/22 8:20 
"""
from pprint import pprint as P
import threading
import time

def hello(num):
    time.sleep(5)
    print('hello %s' %num)

if __name__ == '__main__':
    t1 = threading.Thread(target=hello, args=(10,))
    t1.start()
    t2 = threading.Thread(target=hello, args=(9,))
    t2.start()

    print('ending...')



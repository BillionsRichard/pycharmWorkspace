# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 多线程利器-队列demo01.py 
@time: 2018/5/27 16:10 
"""
from pprint import pprint as P
import threading, time

l = [1, 2, 3, 4, 5]


def remove_ele(l):
    while l:
        a = l[-1]
        P('removing...%s' % a)
        time.sleep(1)
        l.remove(a)


t1 = threading.Thread(target=remove_ele, args=(l,))
t2 = threading.Thread(target=remove_ele, args=(l,))

t1.start()
t2.start()

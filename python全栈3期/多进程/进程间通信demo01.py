# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 进程间通信demo01.py 
@time: 2018/5/29 8:19 
"""
from pprint import pprint as P
import multiprocessing
import time, os


def foo(q):
    P('foo id q:%s' % id(q))
    q.put('foo')
    q.put('123')


if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=foo,args=(q,))
    p.start()

    P('main id q:%s' % id(q))
    P('q.get:%s' % q.get())
    P('q.get:%s' % q.get())

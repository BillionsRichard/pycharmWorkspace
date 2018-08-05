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
import queue # 线程队列

q = queue.Queue(5) #FIFO
    #= [1, 2, 3, 4, 5]
q.put(12)
q.put('sam')
q.put('eva')
q.put((1,2))
q.put({'eva': 1.5}, block=False) # 如果满了则不阻塞，抛出异常。

while q:
    data = q.get(block=False)# 如果空了则不阻塞，抛出异常。
    print(data)
    P('-------')
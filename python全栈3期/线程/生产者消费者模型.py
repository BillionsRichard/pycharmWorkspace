# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 生产者消费者模型.py 
@time: 2018/5/27 17:05 
"""
from pprint import pprint as P
import time,threading,queue,random

q = queue.Queue()

def producer(name):
    count = 0

    while count < 10:
        print('making baozi....')
        time.sleep(random.randrange(5))
        print('%s 生产了包子%s' %(name, count))
        q.put('包子%s' % count)
        count += 1


def consumer(name):
    count = 0

    while count < 10:
        time.sleep(random.randrange(4))
        if not q.empty():
            bz = q.get()
            print('%s 吃了%s' %(name, bz))
        else:
            print('没有包子...')
        count += 1


p1 = threading.Thread(target=producer, args=('sam',))
c1 = threading.Thread(target=consumer, args=('eva',))

p1.start()
c1.start()





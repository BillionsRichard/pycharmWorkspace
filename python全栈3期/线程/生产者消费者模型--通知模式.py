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

        q.task_done() # 通知包子生产完成。
        count += 1


def consumer(name):
    count = 0

    while count < 10:
        print('Waiting....')
        q.join() #等待包子生成

        bz = q.get()
        time.sleep(random.randrange(2))
        print('%s 吃了%s' %(name, bz))

        count += 1


p1 = threading.Thread(target=producer, args=('sam',))
c1 = threading.Thread(target=consumer, args=('eva',))
c2 = threading.Thread(target=consumer, args=('mom',))

p1.start()
c1.start()
c2.start()





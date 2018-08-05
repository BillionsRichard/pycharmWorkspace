# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 死锁demo01.py 
@time: 2018/5/27 15:19 
"""
from pprint import pprint as P
import time,threading

lock = threading.RLock()

class MyThread(threading.Thread):
    def action_A(self):
        with lock:
            P('%s got lock in action_A %s' % (self.name, time.ctime()))
            time.sleep(2)

            with lock:
                P('%s got lock again in action_A %s' %(self.name,  time.ctime()))
                time.sleep(1)

    def action_B(self):
        with lock:
            P('%s got lock in action_B %s' % (self.name, time.ctime()))
            time.sleep(2)

            with lock:
                P('%s got lock again in action_B %s' % (self.name, time.ctime()))
                time.sleep(1)

    def run(self):
        self.action_A()
        self.action_B()


for i in range(5):
    t = MyThread()
    t.start()


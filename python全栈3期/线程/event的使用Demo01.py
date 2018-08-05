# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: event的使用Demo01.py 
@time: 2018/5/27 15:42 
"""
from pprint import pprint as P
import threading,time

class Worker(threading.Thread):
    def run(self):
        print('worker %s event status1:%s' % (self.getName(), event.is_set()))
        event.wait()
        print('%s: 哎。。命苦啊！' % self.getName())
        print('worker %s event status2:%s' % (self.getName(), event.is_set()))
        time.sleep(2)
        event.clear()# 只有clear，才能再次阻塞。

        print('worker %s event status3:%s' % (self.getName(), event.is_set()))
        event.wait()
        print('下班啦。。。')


class Boss(threading.Thread):
    def run(self):
        print('今天晚上加班到12：00下班。。。')
        print('boss event status1:%s' % event.is_set())

        event.set()
        time.sleep(10)

        print('大家都下班吧。。。')
        print('boss event status2:%s' % event.is_set())
        event.set()



if __name__ == '__main__':
    event = threading.Event()

    for i in range(5):
        worker = Worker()
        worker.start()

    boss = Boss()
    boss.start()

    print('%s ending...' % threading.current_thread().getName())
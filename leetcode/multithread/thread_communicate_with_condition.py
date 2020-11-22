# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/5/16 15:52
"""

import threading


# 生产者类
class Producer(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self, name=thread_name)

    def run(self):
        global x
        # 获得锁

        with cond:
            if x == 20:
                cond.wait()

            print("\nProducer: ", end=" ")
            for i in range(20):
                print(x, end=" ")
                x = x + 1
            print(x)
            cond.notify()


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self, name=thread_name)

    def run(self):
        global x
        with cond:
            if x == 0:
                cond.wait()

            print("\nConsumer: ", end=" ")

            for i in range(20):
                print(x, end=" ")
                x = x - 1
            print(x)
            cond.notifyAll()
            # 释放锁


# 创建锁
cond = threading.Condition()
x = 0
p = Producer("Producer")
c = Consumer("Consumer")
p.start()
c.start()
p.join()
c.join()
print("After Producer and Consumer all done:", x)

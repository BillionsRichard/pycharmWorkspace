# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 信号量demo01.py 
@time: 2018/5/27 16:07 
"""
from pprint import pprint as P
import time,threading

class MyThread(threading.Thread):
    def run(self):
        with semaphore:
            time.sleep(2)
            print('%s end.' % self.getName())



if __name__ == '__main__':
    semaphore = threading.Semaphore(5) # 只能有5个线程进入。

    for i in range(20):
        MyThread().start()


# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 多进程启动方式2.py 
@time: 2018/5/27 18:28 
"""
from pprint import pprint as P
import multiprocessing, os,time

cpu_count = os.cpu_count()
print('cpu count:%s---%s' % (cpu_count, time.ctime()))

class MyProcess(multiprocessing.Process):
    def run(self):
        print('%s---%s' % (self.name, os.getpid()))


if __name__ == '__main__':
    for i in range(cpu_count):
        p = MyProcess() # 开启8个子进程，分别启动8个python解释器进程执行之。
        # p.daemon = True
        p.start()
        # p.join() # 等待子进程结束

    print('%s ending.....' % multiprocessing.Process.__name__)
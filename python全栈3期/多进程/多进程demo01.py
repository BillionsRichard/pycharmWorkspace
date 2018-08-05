# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 多进程demo01.py 
@time: 2018/5/27 17:59 
"""
from pprint import pprint as P
import multiprocessing, os,time

cpu_count = os.cpu_count()
print('cpu count:%s---%s' % (cpu_count, time.ctime()))


def process_fun(i):
    time.sleep(20)
    print('%s---%s' % (os.getpid(), i))


if __name__ == '__main__':
    for i in range(cpu_count):
        p = multiprocessing.Process(target=process_fun, args=(i,)) # 开启8个子进程，分别启动8个python解释器进程执行之。
        p.start()

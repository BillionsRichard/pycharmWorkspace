# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 父进程与子进程.py 
@time: 2018/5/28 8:38 
"""
from pprint import pprint as P
import os,multiprocessing,time

def info(title):
    P(title)
    P('parent process:%s' % os.getppid())# pycharm.exe进程
    P('pid:%s' % os.getpid())

def f(name):
    info('function f')
    P('hello %s' % name)


if __name__ == '__main__':
    info('main process line...')
    time.sleep(1)
    P('-----------------------')
    p = multiprocessing.Process(target=info, args=('yuan',))
    p.start()
    p.join()

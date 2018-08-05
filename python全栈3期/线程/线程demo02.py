# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 线程demo02.py 
@time: 2018/5/22 8:30 
"""
from pprint import pprint as P
import threading,time

def music():
    print('begin to listen:%s' % time.ctime())
    time.sleep(2)
    print('end listening..')

def game():
    print('begint to play game:%s' % time.ctime())
    time.sleep(5)
    print('end playing game...')


if __name__ == '__main__':
    t1 = threading.Thread(target=music)
    t2 = threading.Thread(target=game)

    t1.start()
    t2.start()

    t1.join()
    t2.join(1)

    print('main thread ending..')

    # l = []
    # for i in range(2):
    #     t = threading.Thread(target=music)
    #

# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 协程demo01.py 
@time: 2018/6/2 10:32 
"""
from pprint import pprint as P

"""
协程的优势:
1、没有切换的消耗。
2、没有锁的概念。

有一个问题：能用多核么？ 可以采用多进程 + 协程，一个很好的解决并发的方案。

协程主要解决IO操作。
"""


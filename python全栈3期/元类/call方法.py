# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: call方法.py 
@time: 2018/5/20 18:38 
"""
from pprint import pprint as P

class Foo:
    def __call__(self, *args, **kwargs):
        print('call 方法执行啦...%s, %s, %s' %(self, args, kwargs))

f = Foo()


f()
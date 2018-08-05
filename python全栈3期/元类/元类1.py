# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 元类1.py 
@time: 2018/5/20 17:38 
"""
from pprint import pprint as P

class MyType(type):
    def __init__(self, a, b, c):
        print('自定制的元类构造函数被执行。。。')
        print(a, type(a))
        print(b, type(b))
        print(c, type(c))

    def __call__(cls, *args, **kwargs):
        print('self:%s, args:%s, kwargs:%s' %(cls, args, kwargs))
        obj = object.__new__(cls)

        cls.__init__(obj, *args, **kwargs)
        return obj

class Foo(metaclass=MyType): # Foo = MyType('Foo', (,) {}),
    def __init__(self,name):
        print('Foo.__init__ called.')
        self.name = name

f = Foo('sam')
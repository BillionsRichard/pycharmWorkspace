# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: item系列函数.py 
@time: 2018/5/14 8:30 
"""

class Foo:
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        print('getitem')
        return self.__dict__.get(item)

    def __setitem__(self, key, value):
        print('setitem')
        self.__dict__.setdefault(key, value)


    def __delitem__(self, key):
        print('delitem')
        self.__dict__.pop(key)


f = Foo('sam')
print(f.__dict__)

f['h'] = 'ok'
print(f.__dict__)
print(f.h)
print(f['h'])
print(f['notexist'])
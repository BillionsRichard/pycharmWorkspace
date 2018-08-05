# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 下划线开头的attr方法.py 
@time: 2018/5/13 16:56 
"""
from pprint import pprint as pp

class Foo:
    x = 1

    def __init__(self, y):
        self.y = y # 实例化赋值时也会出发__setattr__


    def __getattr__(self, item): #get 的属性不存在时才执行。不定义会执行默认的（抛出AttributeError异常）
        print('执行__getattr__')


    def __delattr__(self, item): # 删除属性时会被调用。
        print('执行__delattr__方法。 ')
        self.__dict__.pop(item)


    def __setattr__(self, key, value): # 属性赋值时会被调用。
        print('__setattr__ called..')
        # self.key = value # 此语句会造成无限递归。
        self.__dict__[key] = value


class Bar:
    pass


f1 = Foo(10)
# print(f1.y)
#
# print(getattr(f1, 'y'))
# print(getattr(f1, 'ooxx'))#get 的属性不存在时才执行 __getattr_方法。

# del f1.y
# print('f1.y: %s' % f1.y)
#
#
# f1.d = 10
# print(f1.__dict__)
#
# pp(dir(Bar))

f1.x = 50

pp(f1.__dict__)

del f1.x

pp(f1.__dict__)

Foo.aaa = 1
print(Foo.aaa)
del Foo.aaa
# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 利用描述符自定制property.py 
@time: 2018/5/20 16:02 
"""
from pprint import pprint as P

class LazyProperty:
    def __init__(self, func):
        # print('------------>%s' %func)
        self.func = func

    def __get__(self, instance, owner): # 未定义__set__方法，为非数据描述符。
        print('__get__ called..[%s].....[%s]' % (instance, owner))
        if instance is None:
            return self

        res = self.func(instance)
        setattr(instance, self.func.__name__, res) # 第一次计算，后续从实例属性中取。
        return res


class Room:
    def __init__(self, name, lenght, width):
        self.name = name
        self.length = lenght
        self.width = width

    # @property # ===> area = property(area)
    @LazyProperty # ===> area = LazyProperty(area) #这就是描述符。
    def area(self):
        return self.width * self.length

    @LazyProperty
    def test(self):
        return 'test'

r1 = Room('wc', 1, 1)
# P(Room.__dict__)
# print(r1.__dict__)
P(r1.area)
P(Room.area)
# P(Room.test)
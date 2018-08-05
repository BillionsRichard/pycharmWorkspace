# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 描述符demo01.py 
@time: 2018/5/20 10:21 
"""

"""
描述符必须被定义成新式类，被代理的类也必须是新式类。

必须把描述符定义成这个类的类属性（非实例属性）



数据描述符：至少实现了__get__ & __set__方法。
非数据描述符：未实现__set__方法。


"""

# def test(x):
#     print('-------->', x)
#
# test('alex')
# test(13)
from pprint import pprint as P

class Typed:
    def __init__(self, field_name, expected_type):
        self.field_name = field_name
        self.field_type = expected_type

    def __get__(self, instance, owner):
        print('__get__ called.')
        print('self:%s,instance:%s,owner:%s' % (self, instance, owner))
        return instance.__dict__[self.field_name]


    def __set__(self, instance, value):
        print('__set__ called.')
        print('self:%s, instance:%s,value:%s' % (self, instance, value))
        if not isinstance(value, self.field_type):
            raise TypeError('%s expected type:%s, but input type:%s' % (self.field_name, self.field_type, type(value)))
        else:
            instance.__dict__[self.field_name] = value



class People:
    name = Typed('name',  str)
    age = Typed('age', int)
    salary = Typed('salary', float)

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


p1 = People('egon', 18, 20000.)
p1.name

# P(p1.__dict__)
# P(People.__dict__)
P(p1.__dict__)
p1.name = 'sam'
P(p1.__dict__)
# p2 = People(23.0, 25, 200002.0)


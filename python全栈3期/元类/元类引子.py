# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 元类引子.py 
@time: 2018/5/20 17:20 
"""
from pprint import pprint as P

class Foo:
    pass

class Bar:
    pass

# f1 = Foo()
#
# print(type(f1))
# print(type(Foo))
# print(type(Bar))

def __init__(self, name, age):
    self.name = name
    self.age = age


FFo = type('FFo', (object,), {'x':1, '__init__': __init__})

print(type(FFo))
P(FFo.__dict__)
# f1 = type(FFo)
#
# print(f1.x)
#
ff1 = FFo('sam', 32)
P(FFo.__dict__)
print(ff1.name)
print(ff1.age)
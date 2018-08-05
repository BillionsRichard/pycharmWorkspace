# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: isinstance和issubclass.py 
@time: 2018/5/13 22:55 
"""
class Foo:
    pass

class Bar(Foo):
    pass


f1 = Foo()
print(isinstance(f1, Foo))

print(issubclass(Bar, Foo))

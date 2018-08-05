# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 类的doc属性无法继承.py 
@time: 2018/5/16 8:19 
"""

class Foo:
    """doc text of Foo class.

    """
    pass

class Bar(Foo):
    bar = 'bar'
    pass

print(Foo.__doc__)
print(Bar.__doc__)

print(Foo.__dict__)
print(Bar.__dict__)
Bar.__dict__.pop('bar')
print(Bar.__dict__)

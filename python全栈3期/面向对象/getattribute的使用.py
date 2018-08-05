# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: getattribute的使用.py 
@time: 2018/5/14 0:18 
"""

class Foo:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item): # 当找不到属性时（__getattribute__抛出异常时）调用。
        print('__getattr__ called...')
        print('%s not exist' % item)
        return None

    # def __getattribute__(self, item): # 调用对象的属性时首先会被调用。
    #     print('__getattribute__ called...')
    #     #
    #     # if hasattr(self, item):
    #     #     # return getattr(self, item) # 循环递归。
    #     #     return self.__dict__[item]
    #     # else:
    #     #     raise AttributeError
    #     raise AttributeError



f = Foo('sam')

print(f.name)
print(f.age)
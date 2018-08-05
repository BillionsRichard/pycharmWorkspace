# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: __str__方法的使用.py 
@time: 2018/5/14 8:38 
"""
l = list('hello')
print(l)

class Foo:
    def __init__(self,name, age):
        self.name = name
        self.age = age


    def __str__(self):
        # return super().__str__()
        # return 2# 必须返回字符串。
        return 'STR: name:%s,age:%s' % (self.name, self.age)


    def __repr__(self):
        # return super().__str__()
        # return 1 # 必须返回字符串。
        return 'REPR: name:%s,age:%s' % (self.name, self.age)

f = Foo('sam', 32)

print(f)# ===> str(f) ===> f.__str__ ==找不到===> f.__repr__()

# f1 = open('a.txt', 'w+')
# print(f1)
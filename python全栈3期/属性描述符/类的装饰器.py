# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 类的装饰器.py 
@time: 2018/5/20 11:31 
"""
from pprint import pprint as P

def deco(obj):
    print('------------------%s' % obj)
    obj.x = 1
    obj.y = 1
    obj.z = 1
    return obj

@deco # test = deco(test), 装饰器等价于高阶函数。
def test():
    '''test fun'''

    print('test函数运行。')
P(test.__dict__)
# test()

# @deco # Foo = deco(Foo)
# class Foo:
#     pass
#
# f1 = Foo()
# print(f1.__dict__)
# P(Foo.__dict__)
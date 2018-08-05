   # encoding: utf-8

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 类的装饰器-修订版.py 
@time: 2018/5/20 12:18 
"""
from pprint import pprint as P

def Typed(**kwargs):
    print('111:%s' % kwargs)
    def deco(obj):
        for k,v in kwargs.items():
            setattr(obj, k, v)

        return obj
    return deco

@Typed(name='egon', age=30) # ==>1、Typed(x=1,y=2,z=3)-->deco. 2、@deco(Foo)
class Foo:
    pass

P(Foo.__dict__)

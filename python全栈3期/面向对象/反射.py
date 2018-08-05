# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com
@site:  
@software: PyCharm 
@file: 反射.py 
@time: 2018/5/13 15:04 
"""
from pprint import pprint as pp

class BlackMedium:
    feature = 'Ugly'

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def sell_house(self):
        print('%s 正在买房子，傻逼才买呢' %self.name)

    def rent_house(self):
        print('%s 正在租房子，傻逼才租呢' %self.name)


b1 = BlackMedium('大唐中介', '顺江小区')

# print(hasattr(b1, 'name'))
# print(hasattr(b1, 'sell_house'))
#
# name = getattr(b1, 'name')
# print(name)
#
# sell_house_f = getattr(b1, 'sell_house')
# sell_house_f()
#
# print(hasattr(b1, 'ooxx'))
#
# rent_house_f = getattr(b1, 'rent_house1', '无此函数')
# print(rent_house_f)
#
# pp(b1.__dict__)
# setattr(b1, 'sb', True)
# pp(b1.__dict__)
#
# delattr(b1, 'sb')
# pp(b1.__dict__)

setattr(b1, 'func', lambda x:x+1) # 只是给对象添加了属性，类并没有。
pp(BlackMedium.__dict__)
pp(b1.__dict__)

# f = getattr(b1, 'func')
# print(f(2))
#
# print(b1.func(10))
# pp(b1.__dict__)

print(hasattr(BlackMedium, 'feature')) # 类本质也是对象。



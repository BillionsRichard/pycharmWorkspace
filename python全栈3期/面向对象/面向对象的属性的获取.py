#coding:utf-8

"""
__dict__：返回类实例的数据属性字典

dir(ClassName)：

注意：1、实例只有数据属性，但是可以访问类的属性
    访问过程：现在实例的字典中找，找不到时再到类的属性字典中找。

    2、类中定义的方法不属于实例的，是类的。通过实例可以调用类的方法，类会自动把实例作为第一次参数，作为self实参。

    3、给实例增加的外部函数属性（通过赋值形式增加），通过实例调用时，实例不会被自动填充，需要显式传递实例参数。

"""
from pprint import pprint as pp

class Chinese(object):
    """中国人类
    """

    dang = '共产党'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print('from _init__: %s' % Chinese.dang)

    def eat():
        print('中国人在吃饭....')

    def cha_dui(self):
        print('中国人在插队...')


print(Chinese.dang)
pp(Chinese.__dict__)
pp(type(Chinese.__dict__))

pp(dir(Chinese))
pp(type(dir(Chinese)))

print(Chinese.__name__)
print(Chinese.__doc__)
print(Chinese.__bases__)
print(Chinese.__module__)

print('__init__方法的应用'.center(120, '*'))
p1 = Chinese('sam', 32, 'male')
print(p1)
print(p1.__dict__)
pp(Chinese.__dict__)

Chinese.eat()
Chinese.country = 'China'
p1.cha_dui()
print(p1.dang)
print(p1.country)

del Chinese.dang
print(p1.dang)

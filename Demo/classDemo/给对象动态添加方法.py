#coding:utf-8
from types import  MethodType

class Person(object):
    def __init__(self):
        pass

p = Person()

p.name = 'jerry'

print(p.name)

def say(obj):
    print('my name is:' + obj.name)

p.speak = MethodType(say, p)
p.speak()

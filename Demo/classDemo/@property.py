#coding:utf-8

class Person(object):
    def __init__(self, age):
        self.__age = age

    # def getAge(self):
    #     return self.__age
    @property
    def age(self):
        print('getter called')
        return self.__age

    @age.setter
    def age(self, age):
        print('setter called')
        self.__age = age if age >0 else 0

p = Person(18)

print(p.age)
p.age = -1
print(p.age)
p.age = 31
print(p.age)

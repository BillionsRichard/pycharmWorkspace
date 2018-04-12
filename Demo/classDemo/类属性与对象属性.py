#coding:utf-8

class Person(object):
    name = "person"

    def __init__(self, name):
        self.name = name
        pass



p = Person('jerry')

print(p.name)
print(Person.name)
del p.name
print(p.name)
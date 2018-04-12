class Foo(object):
    __slots__ = ('name', 'age')
    def __init__(self):
        print('Foo init')


f1 = Foo()
f1.name = 'sam'
f1.age = 20
f1.gender = 'Femal'


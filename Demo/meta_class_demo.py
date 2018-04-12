from pprint import pprint as pp


class MyType(type):
    def __init__(cls, names, bases, dic):
        print('MyType created')

    def __call__(cls, *args, **kwargs):
        print('MyType called')


class Foo:
    __metaclass__ = MyType

    def __init__(self):
        print('Foo inited')

    def fun(self):
        print('calling fun')

    def __call__(self, *args, **kwargs):
        print('called')
        print(args)
        print(kwargs)


f = Foo()
# pp(dir(Bar))
# pp(f)
# pp(dir(f))
# pp(f.__metaclass__)
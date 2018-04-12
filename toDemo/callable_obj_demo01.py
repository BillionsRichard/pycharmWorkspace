from pprint import pprint as pp
class Foo:
    def __init__(self):
        print('inited')

    def fun(self):
        print('calling fun')

    def __call__(self, *args, **kwargs):
        print('called')
        print(args)
        print(kwargs)

f = Foo()
f.fun()
f(1,2,3, a=1,b=2)
print(type(f))
print(type(type(f)))
print(type(Foo))

Bar = type('Bar', (Foo,), {'name':'sam', 'age':18})
print(type(Bar))
b = Bar()
print(b.name, b.age)
b.fun()

pp(dir(Bar))
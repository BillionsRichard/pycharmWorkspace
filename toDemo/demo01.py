class Foo:
    def __init__(self, name):
        self.name = name

    def fun1(self):
        print('fun1')


def fun2(arg):
    print(arg)


Foo.fun2 = fun2

f = Foo('ok')
f.fun2()
f.age = 18
print(f.age)

print('*'*20)
f1 = Foo('bad')
print(f1.age)

f1.fun2()

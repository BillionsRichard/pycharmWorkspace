from functools import  partial
from functools import  wraps
from pprint import  pprint as p

# def add(a, b):
#     return a+b
#
# print(add)
#
# plus3 = partial(add, 3)
#
# print(plus3)
# p(dir(plus3))
# p(plus3.args)
# p(plus3.func)
# p(plus3.keywords)
#
# p(plus3(5))


p('---'*20)

def my_dectorator(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        print('decoratored func called')
        return f(*args, **kwargs)
    return wrap


@my_dectorator
def ff():
    """ff doc string"""
    print('ff called.')

@my_dectorator
def g():
    print('g called.')

p(ff.__name__)
p(ff.__doc__)
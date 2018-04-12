from functools import  wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator1 called')
        result = func(*args, **kwargs)
        return  result
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator2 called')
        result = func(*args, **kwargs)
        return  result
    return wrapper


@decorator2
@decorator1
def add(a, b):
    return a+b

print(add(3,5))
print('*'*80)
print(add.__wrapped__(3,5))
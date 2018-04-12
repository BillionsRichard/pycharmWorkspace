from functools import wraps
import logging


def logged(level, name=None, msg=None):
    def decorate(func):
        logname = name if name else func.__module__
        logmsg = msg if msg else func.__name__
        log = logging.getLogger(logname)

        @wraps(func)
        def inner(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return inner
    return decorate


@logged(logging.INFO)
def add(a, b):
    return a+b

@logged(logging.ERROR)
def spam():
    print('spam')


add(3,5)
print('*'*100)
spam()

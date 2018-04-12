from functools import  wraps
import  time
from  inspect import  signature

def timethis(func):
    @wraps(func)
    def warapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(func.__name__, end_time-start_time)
        return result
    return  warapper


@timethis
def count_down(n):
    """Count down doc string."""
    while n>0:
        n-=1

count_down(10)
# count_down(100000000)
print(count_down.__doc__)
print(count_down.__name__)
print(count_down.__annotations__)
print(signature(count_down))
print(count_down.__wrapped__(1000))




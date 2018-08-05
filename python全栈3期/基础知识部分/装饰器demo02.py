import time1


def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time1.time()
        ret = func(*args, *kwargs)
        end_time = time1.time()
        print('函数的运行时间:%s' % (end_time-start_time))
        return ret
    return wrapper


@timmer
def cal(n):
    tot = 0
    for i in range(n):
        time1.sleep(0.1)
        tot += i

    return tot

print(cal(30))


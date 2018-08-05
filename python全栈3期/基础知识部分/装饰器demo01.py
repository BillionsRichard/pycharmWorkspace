import time1

def cal(n):
    start = time1.time()
    tot = 0
    for i in range(n):
        tot += i

    end = time1.time()
    times = end - start
    print('函数的运行时间:%s' % times)
    return tot


print(cal(1000))

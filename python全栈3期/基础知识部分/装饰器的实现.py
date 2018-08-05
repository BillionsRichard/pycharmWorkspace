import time1

"""
装饰器的架子

"""


def timmer(func):
    def wrapper():
        st = time1.time()
        func()
        ed = time1.time()
        print('运行时间是：%s' % (ed - st))

    return wrapper


@timmer# 相当于 test = timmer(test)
def test():
    time1.sleep(3)
    print('test函数运行完毕')



test()

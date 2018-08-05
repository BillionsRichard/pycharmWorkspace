#coding:utf-8

import time1

"""
装饰器的架子

"""


def timmer(func):
    def wrapper():
        st = time1.time()
        rt = func()
        ed = time1.time()
        print('运行时间是：%s' % (ed - st))
        return rt

    return wrapper


@timmer# 相当于 test = timmer(test)
def test():
    time1.sleep(3)
    print('test函数运行完毕')
    return 'test的返回值'



ret1 = test()
print(ret1)

#coding:utf-8

import time1

"""
装饰器的架子

"""


def timmer(func):
    def wrapper(*args, **kwargs):
        st = time1.time()
        rt = func(*args, **kwargs)
        ed = time1.time()
        print('运行时间是：%s' % (ed - st))
        return rt

    return wrapper


@timmer# 相当于 test = timmer(test)
def test(name, age):
    time1.sleep(3)
    print('test函数运行完毕, 名字是[%s], 年龄是[%s]' % (name, age))
    return 'test的返回值'


@timmer# 相当于 test = timmer(test)
def test1(name, age, gender):
    time1.sleep(3)
    print('test1函数运行完毕, 名字是[%s], 年龄是[%s], 性别[%s]' % (name, age, gender))
    return 'test1的返回值'



ret1 = test('sam', 18)
print(ret1)


ret2 = test1('sam', 28, '男')
print(ret2)

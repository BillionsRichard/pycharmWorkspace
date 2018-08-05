# coding:utf-8

"""
高阶函数定义：
    满足以下条件之一即为“高阶函数”
    1、函数参数是一个函数名。
    2、函数的返回值是一个函数名。

"""

import time1


def foo():
    time1.sleep(2)
    print('你好啊，嘉慧儿...')


def test(func):
    print(func)
    start_time = time1.time()
    func()
    end_time = time1.time()
    print('函数的运行时间是：%s' % (end_time - start_time))


test(foo)#修改函数的调用方式。，不修改函数的调用方式。

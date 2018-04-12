#coding:utf-8
import threading

import time
'''
多进程中，同一个变量有多份拷贝在不同的进程中；互不共享；

多线程中；所有变量都由不同线程共享；任何一个变量可以被任意一个线程修改；

'''
num = 0

'''
创建一个全局的ThreadLocal对象，
每个线程有独立的存储空间
每个线程对ThreadLocal对象都可以读写，但是互不影响。

'''
local = threading.local()


def run(x, n):
    x = x + n
    x = x - n


def func(n):
    # 每个线程都有local.x，就是线程的局部变量

    local.x = num
    for i in range(10000000):
        run(local.x, n)

    print("%s->%d" % (threading.current_thread().getName(), local.x))


if __name__ == '__main__':
    t1 = threading.Thread(target=func, args=(6,))
    t2 = threading.Thread(target=func, args=(9,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('主线程结束，num=%d' % num)

'''
作用：为每个线程绑定的一个数据库链接，HTTP请求，用户身份标识信息等；
这样每个线程的所有调用到的处理函数都可以非常方便的访问这些资源。
'''
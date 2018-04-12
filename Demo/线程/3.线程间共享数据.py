#coding:utf-8
import threading
import time
'''
多进程中，同一个变量有多份拷贝在不同的进程中；互不共享；

多线程中；所有变量都由不同线程共享；任何一个变量可以被任意一个线程修改；

'''
num = 0

def run(n):
    global num

    for i in range(1000000):
        num += i
        num -= i


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(6,))
    t2 = threading.Thread(target=run, args=(9,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('主线程结束，num=%d' % num)

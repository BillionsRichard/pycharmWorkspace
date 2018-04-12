#coding:utf-8

from multiprocessing import Process
from multiprocessing import Queue
import os
import time

def write(q):
    print('写子进程启动%d' %(os.getpid()))

    for chr in ['A', 'B', 'C', 'D']:
        q.put(chr)
        time.sleep(1)


def read(q):
    print('读子进程启动%d' %(os.getpid()))

    while True:
        val = q.get(True)
        print('Read data: %s' %(val))

    print('读子进程结束%d' %(os.getpid()))


if __name__ == '__main__':
    print('父进程启动....')
    q = Queue()

    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()

    pr.terminate()
    # pr.join()

    print('父进程结束....')

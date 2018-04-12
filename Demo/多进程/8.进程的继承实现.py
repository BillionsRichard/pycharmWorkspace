#coding:utf-8
from multiprocessing import Process
import time
import os

class SamProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print('子进程启动....%s' % self.name)
        time.sleep(1.5)
        print('子进程结束....%s' % self.name)


if __name__ == '__main__':
    print('父进程启动>....')

    p = SamProcess('sam')
    p.start()
    p.join()

    print('父进程结束...')

import os
import time
from multiprocessing import Process

def run(adj):
    print('pid:%d--ppid:%d' %(os.getpid(), os.getppid()))
    while True:
        print('sam is a %s man' % (adj))
        time.sleep(1.65)

if __name__ == '__main__':
    print('pid:%d' %(os.getpid()))

    p = Process(target=run, args=('hansome',))
    p.start()

    while True:
        print('sam is a good man')
        time.sleep(1.3)

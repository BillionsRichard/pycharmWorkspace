from multiprocessing import Pool
import time
import os
import random

def run(i):
    print('子进程%d启动...%d' %(i, os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,1.1, 1.2, 1.3, 1.4]))
    end = time.time()
    print('子进程%d结束...%d, 耗时%.2fs' % (i, os.getpid(), end-start))


if __name__ == '__main__':
    print('父进程启动...')
    start = time.time()

    pp = Pool(15)

    for i in range(20):
        #创建进程，放入进程池统一管理
        """
        apply:同步启动，顺序启动。一个执行完毕后执行下一个。
        apply_async:异步启动，同时启动，并发执行。
        """
        pp.apply(run, args=(i,))

    pp.close()
    pp.join()

    end = time.time()
    print('父进程结束,耗时%.2fs...' %(end-start))
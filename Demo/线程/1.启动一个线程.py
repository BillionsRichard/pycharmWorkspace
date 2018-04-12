#coding:utf-8

import threading
import time

def run(num):
    threading.current_thread().setName('thread-%s' %num)
    print('子线程%s启动了...' % threading.current_thread().getName())

    time.sleep(2)

    print('子线程%s结束了...' % threading.current_thread().getName())


if __name__ == '__main__':
    # 任何进程启动都会默认启动一个线程（主线程）
    print('主线程启动了...%s' % threading.current_thread().name)

    # t = threading.Thread(target=run, name='subThread')
    t = threading.Thread(target=run, args=(1,))

    t.start()
    t.join()

    print('主线程%s结束了....' % threading.current_thread().getName())
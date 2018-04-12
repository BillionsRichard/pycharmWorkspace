#coding:utf-8
import threading
num = 0
lock = threading.Lock()

def run(n):
    global num,lock

    for i in range(1000000):
        # lock.acquire()
        #
        # try:
        #     num = num +i
        # finally:
        #     lock.release()
        #
        # lock.acquire()
        #
        # try:
        #     num = num -i
        # finally:
        #     lock.release()
        with lock:
            num += i

        with lock:
            num -= i


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(6,))
    t2 = threading.Thread(target=run, args=(9,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('num=%d' % (num))
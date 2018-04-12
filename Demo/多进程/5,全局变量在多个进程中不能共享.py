from multiprocessing import Process
import time

d = dict(num=100)


def run():
    global d
    print('子进程启动....%d' %d.get('num'))

    d['num'] = d.get('num') + 1
    print('子进程结束....%d' %d.get('num') )


if __name__ == '__main__':
    print('父进程启动....%d' %d.get('num'))

    p = Process(target=run)
    p.start()
    p.join()

    p1 = Process(target=run)
    p1.start()
    p1.join()

    print('父进程结束...%d' %d.get('num'))
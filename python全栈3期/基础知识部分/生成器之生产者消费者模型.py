# coding:utf-8

import time1


def consumer(name):
    print('%s 准备开始消费。。。。' % name)
    while True:
        product = yield #循环接受生产者发送过来的产品，进行消费。第一次迭代后，挂在此处；第二次迭代阶段会先进行赋值，然后再循环一次）
        print('%s 消费了【%s】' % (name, product))#第一次迭代并不会被执行。。。。


def producer():
    c1 = consumer('sam')
    c2 = consumer('eva')

    c1.__next__() #第一次迭代，函数停留在yield之后，下一次通过send触发迭代，导致product接收send过来的值
    c2.__next__() #第一次迭代

    for product_id in range(2):
        print('生产者开始生产【包子%s】。。。' % product_id)
        time1.sleep(4)
        if product_id % 2 == 0:
            c1.send('包子%s' % product_id)
        else:
            c2.send('包子%s' % product_id)



if __name__ == '__main__':
    # producer_generator = producer()
    producer()

    # for i in range(5):
    #     product = producer_generator.__next__()
    #     consumer_generator.__next__()
    #     consumer_generator.send(product)



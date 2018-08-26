# encoding: utf-8  

"""
用数组实现队列：


@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: ListQueue.py 
@time: 2018/8/26 15:47 
"""


class ListQueue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        """入队。

        :param data:
        :return:
        """
        self.queue.append(data)
        return

    def dequeue(self):
        """出队

        :return:
        """
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def front_value(self):
        """返回队首的值

        :return:
        """
        if not self.queue:
            return None

        return self.queue[0]

    def is_empty(self):
        """队列是否为空

        :return:
        """
        return not bool(self.queue)

    def traverse(self):
        print('遍历:', self.queue)


if __name__ == '__main__':
    q = ListQueue()
    q.traverse()

    q.enqueue('晓明')
    q.traverse()

    q.enqueue('晓红')
    q.enqueue('晓嘉')
    q.enqueue('晓慧')
    q.traverse()
    q.dequeue()
    q.traverse()
    q.enqueue('小松')
    q.traverse()
    q.dequeue()
    q.traverse()

# encoding: utf-8  

"""
用链表实现队列:
    思想：继承自链表类。
    1）入队：在链表尾部插入元素。
    2）出队：
        1.保存链表头部元素。
        2.删除链表头节点。
        3.返回链表头部元素值。


@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: LinkQueue.py 
@time: 2018/8/26 16:23 
"""
from link.link import Link


class LinkQueue(Link):
    def enqueue(self, data):
        self.insert(data, -1)

    def dequeue(self):
        if self.is_empty():
            return None

        front_val = self.front_value()
        self.delete(front_val)
        return front_val

    def front_value(self):
        """返回队首的值

        :return:
        """
        if self.is_empty():
            return None

        return self.head.next.data


if __name__ == '__main__':
    q = LinkQueue()
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

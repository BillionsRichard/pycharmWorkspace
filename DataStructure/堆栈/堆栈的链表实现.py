# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 堆栈的链表实现.py 
@time: 2018/8/5 14:38 
"""


class Node(object):
    """链表的节点类。

    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkStack(object):
    """堆栈的链表实现。

    """

    def __init__(self, size=10):
        """创建一个堆栈。

        :param size: 堆栈的大小。
        """
        self.MAX_SIZE = size
        self.head = self.create_link()
        self.top = self.head

    def create_link(self):
        """创建堆栈的数据存储结构（链表）

        :return: link head.
        """
        head = Node(None)
        ptr = head
        for i in range(self.MAX_SIZE - 1):
            new_node = Node(None)
            ptr.next = new_node
            ptr = new_node
        ptr.next = None
        return head

    def push(self, data):
        if self.is_full():
            print('Full eror:%s' % data)
            return

        print('pushed:%s' % data)
        self.top.data = data
        self.top = self.top.next
        return

    def pop(self):
        if self.is_empty():
            print('Emtpy error.')
            return None

        ptr = self.head
        while ptr.next != self.top:
            ptr = ptr.next

        pop_data = ptr.data
        self.top = ptr
        print('poped:%s' % pop_data)
        return pop_data

    def is_full(self):
        return self.top is None

    def is_empty(self):
        return self.top == self.head


if __name__ == '__main__':
    ls = LinkStack(10)

    print('is full:%s' % ls.is_full())
    print('is empty:%s' % ls.is_empty())

    ls.push('sam')
    ls.push('cheung')
    ls.push('ada')
    ls.pop()
    ls.push('a')
    ls.push('b')
    ls.push('c')
    ls.push('d')
    ls.push('e')
    ls.push('f')
    ls.push('G')
    ls.push('I')
    ls.push('H')
    ls.push('J')

    while not ls.is_empty():
        ls.pop()

# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 双向链表的实现.py 
@time: 2018/8/4 22:39 
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.last = None


class DoubleLink(object):
    def __init__(self, data):
        self.head = Node(data)
        self.size = 1

    def get_tail(self):
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        return ptr

    def insert(self, data, index=-1):
        node = Node(data)
        print('%s插入%s' % (index, data))
        if index in [-1, self.size]:
            tail = self.get_tail()
            tail.next = node
            node.last = tail
            self.size += 1
            return

        if index == 0:
            node.next = self.head
            node.last = None
            self.head.last = node
            self.head = node
            self.size += 1
            return

        if index not in range(self.size):
            raise Exception('insert position not in range(0, %s)' % self.size)

        cursor_ptr = self.head
        cursor_idx = 1
        while cursor_idx < index:
            cursor_ptr = cursor_ptr.next
            cursor_idx += 1

        nxt_ptr = cursor_ptr.next

        cursor_ptr.next = node
        node.last = cursor_ptr
        node.next = nxt_ptr
        nxt_ptr.last = node

        self.size += 1
        return

    def delete(self, data):
        cursor_ptr = self.head
        print('删除%s...' % data)
        while cursor_ptr:
            if data == cursor_ptr.data:
                break
            cursor_ptr = cursor_ptr.next
        else:
            print('%s not found' % data)
            return

        if cursor_ptr == self.head:
            self.head = cursor_ptr.next
            if not self.head:
                return
            self.head.last = None
            return

        tail = self.get_tail()
        if cursor_ptr == tail:
            cursor_ptr.last.next = None
            return

        left_ptr = cursor_ptr.last
        right_ptr = cursor_ptr.next
        left_ptr.next = right_ptr
        right_ptr.last = left_ptr
        return

    def traverse(self):
        data_list = []
        curor_ptr = self.head
        while curor_ptr:
            data_list.append(curor_ptr.data)
            curor_ptr = curor_ptr.next

        print('遍历结果：%s' % data_list)
        return data_list

    def reverse(self):#[1, 0, 8, 6, 4, 2, -2]
        print('reversing....')
        p = self.get_tail()
        self.head = p
        q = p.last

        while p:
            r = p.next
            q = p.last

            p.next = q
            p.last = r

            r = p
            p = q
            if q:
                q = q.last

        return


def create_double_link(data_itr):
    """从一个可迭代对象生成一个双向链表.

    :param data_itr: 可迭代对象
    :return:
    """
    idx = 0
    head = None
    for data in data_itr:
        if idx == 0:
            head = DoubleLink(data)
        else:
            head.insert(data)
        idx += 1
    return head


if __name__ == '__main__':
    link = create_double_link([0, 8, 3, 4, 2])
    print('初始化')
    link.traverse()

    link.insert(-1, 0)
    link.traverse()

    link.insert(-2, -1)#[-1, 0, 8, 3, 4, 2, -2]
    link.traverse()

    link.insert(100, 4)
    link.traverse()

    link.insert(1, 1)#[-1, 0, 8, 3, 100, 4, 2, -2]
    link.traverse()

    link.insert(6, 4)
    link.traverse()

    link.insert(3, 9)
    link.traverse()

    link.insert(30, 11)  # [-1, 1, 0, 8, 6, 3, 100, 4, 2, 3, -2]
    link.traverse()#[-1, 1, 0, 8, 6, 3, 100, 4, 2, 3, -2, 30]

    # link.insert('error', 13)
    # link.traverse()
    link.delete(-1)
    link.traverse()#[1, 0, 8, 6, 3, 100, 4, 2, 3, -2, 30]

    link.delete(30)  # [1, 0, 8, 6, 3, 100, 4, 2, 3, -2, 30]
    link.traverse()

    link.delete(3)
    link.traverse()

    link.delete(3)
    link.traverse()

    link.delete(100)
    link.traverse()

    link.delete(99)
    link.traverse()# [1, 0, 8, 6, 4, 2, -2]

    link.reverse()#
    link.traverse()

    link.insert('sam')  # [-2, 2, 4, 6, 8, 0, 1]
    link.traverse()

    link.reverse()
    link.traverse()

    link.delete(8)
    link.traverse()

    link.reverse()#
    link.traverse()

    link.reverse()#
    link.traverse()
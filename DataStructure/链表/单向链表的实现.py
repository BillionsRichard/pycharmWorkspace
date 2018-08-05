# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 单向链表的实现.py 
@time: 2018/8/4 10:18 
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Link(object):
    def __init__(self, head):
        """链表初始化，创建一个链表头。

        :param head: 链表头数据
        """

        self.head = Node(head)
        self.size = 1

    def get_tail(self):
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        return ptr

    def insert(self, data, index=-1):
        """链表中插入数据

        插入处理：
        1）头部: 更新头部，链表长度+1
        2）中间：找到插入的前驱节点。
        3）尾部. 更新尾部指针。

        :param data: 要插入的数据
        :param index: 插入的位置，0表示插入到链表头部，-1表示插入末尾。
        :return: None
        """
        if not (index in range(self.size + 1) or index == -1):
            raise Exception('Insert position must be equal to -1 or in [0, %s]' % (self.size + 1))

        node = Node(data)
        print('%s插入%s' % (index, data))
        if index == -1:  # insert at tail
            tail = self.get_tail()
            tail.next = node
            node.next = None
            self.size += 1
            return

        if index == 0:  # insert at head
            node.next = self.head
            self.head = node
            self.size += 1
            return

        # insert at middle
        cursor_index = 1
        cursor_pre = self.head
        while cursor_index < index:
            cursor_pre = cursor_pre.next
            cursor_index += 1

        cursor_pre.next, node.next = node, cursor_pre.next
        self.size += 1
        return

    def delete(self, data):
        cursor = self.head
        cursor_prev = None
        while cursor and cursor.data != data:
            cursor_prev = cursor
            cursor = cursor.next

        if not cursor:
            print('%s not found' % data)
            return

        print('删除%s' % data)
        if cursor == self.head:  # 删除的元素在链表头部。
            self.head = cursor.next
        else:
            cursor_prev.next = cursor.next
        self.size -= 1
        return

    def traverse(self):
        data_list = []
        cursor_ptr = self.head

        print('link list:', end='\t')
        while cursor_ptr:
            # print('[%ls]' % cursor_ptr.data, end='-->')
            data_list.append(cursor_ptr.data)
            cursor_ptr = cursor_ptr.next

        print(data_list)
        return data_list

    def reverse(self):
        """链表的反转.

        :return:
        """
        pre_ptr = self.head
        nxt_ptr = pre_ptr.next
        pre_ptr.next = None # 非常重要，否则会导致遍历出异常。

        while nxt_ptr:
            tmp_ptr = nxt_ptr.next
            nxt_ptr.next = pre_ptr
            pre_ptr = nxt_ptr
            nxt_ptr = tmp_ptr
        self.head = pre_ptr


def create_link(data_itr):
    """从一个可迭代对象生成一个链表.

    :param data_itr: 可迭代对象
    :return:
    """
    idx = 0
    head = None
    for data in data_itr:
        if idx == 0:
            head = Link(data)
        else:
            head.insert(data)
        idx += 1
    return head


if __name__ == '__main__':
    link = create_link([0, 8, 3, 4, 2])
    link.traverse()

    link.insert(-1, 0)
    link.traverse()

    link.insert(-2, -1)
    link.traverse()

    link.insert(100, 4)
    link.traverse()

    link.insert(1, 1)
    link.traverse()

    link.insert(6, 4)
    link.traverse()

    link.insert(3, 9)
    link.traverse()

    link.insert(30, 11)
    link.traverse()

    # link.insert('error', 13)
    # link.traverse()
    link.delete(-1)
    link.traverse()

    link.delete(30)
    link.traverse()

    link.delete(3)
    link.traverse()

    link.delete(3)
    link.traverse()

    link.delete(100)
    link.traverse()

    link.delete(99)
    link.traverse()

    link.reverse()
    link.traverse()

    link.insert('sam')#[-2, 2, 4, 6, 8, 0, 1]
    link.traverse()

    link.reverse()
    link.traverse()

    # link2 = create_link("samcheung")
    # link2.traverse()
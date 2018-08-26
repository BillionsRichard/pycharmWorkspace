# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: link.py 
@time: 2018/8/26 16:24 
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Link(object):
    def __init__(self):
        """链表初始化，创建一个链表头。

        链表头中存放空数据（None），链表大小为0，表示链表为空。

        """

        self.head = Node(None)
        self.size = 0

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
            # node.next = self.head
            # self.head = node
            # self.size += 1
            self.head.next = node
            self.size += 1
            return

        # insert at middle
        cursor_index = 1
        cursor_pre = self.head.next
        while cursor_index < index:
            cursor_pre = cursor_pre.next
            cursor_index += 1

        cursor_pre.next, node.next = node, cursor_pre.next
        self.size += 1
        return

    def delete(self, data):
        # cursor = self.head
        cursor = self.head.next
        # cursor_prev = None
        cursor_prev = self.head
        while cursor and cursor.data != data:
            cursor_prev = cursor
            cursor = cursor.next

        if not cursor:
            print('%s not found' % data)
            return

        print('删除%s' % data)
        # if cursor == self.head:  # 删除的元素在链表头部。
        #     self.head = cursor.next
        # else:
        #     cursor_prev.next = cursor.next
        cursor_prev.next = cursor.next

        self.size -= 1
        return

    def traverse(self):
        data_list = []
        # cursor_ptr = self.head
        cursor_ptr = self.head.next

        print('link list:', end='\t')
        while cursor_ptr:
            # print('[%ls]' % cursor_ptr.data, end='-->')
            data_list.append(cursor_ptr.data)
            cursor_ptr = cursor_ptr.next

        print(data_list)
        return data_list

    def is_empty(self):
        """链表只有链表头时，链表为空。

        :return:
        """
        return self.head.next is None

    def reverse(self):
        """链表的反转.

        :return:
        """
        if self.is_empty():
            return

        pre_ptr = self.head.next
        nxt_ptr = pre_ptr.next
        pre_ptr.next = None  # 非常重要，否则会导致遍历出异常。

        while nxt_ptr:
            tmp_ptr = nxt_ptr.next
            nxt_ptr.next = pre_ptr
            pre_ptr = nxt_ptr
            nxt_ptr = tmp_ptr
        self.head.next = pre_ptr


# def create_link(data_itr):
#     """从一个可迭代对象生成一个链表.
#
#     :param data_itr: 可迭代对象
#     :return:
#     """
#     idx = 0
#     head = None
#     for data in data_itr:
#         if idx == 0:
#             head = Link(data)
#         else:
#             head.insert(data)
#         idx += 1
#     return head
if __name__ == '__main__':
    h = Link()
    h.insert(0)
    h.insert(1)
    h.insert(2)
    h.insert(3)
    h.insert(4)
    h.insert(5)
    h.traverse()
    h.reverse()
    h.traverse()
    h.insert('ok', 2)
    h.traverse()

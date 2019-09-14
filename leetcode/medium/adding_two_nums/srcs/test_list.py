# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/1 11:49 
"""

from medium.adding_two_nums.srcs.answer import ListNode
from medium.adding_two_nums.srcs.answer import get_list_value
import unittest


class TestListNode(unittest.TestCase):
    def setUp(self):
        print('ListNode setting up')

    def tearDown(self):
        print('ListNode tearing down..')

    def test_list1(self):
        head = ListNode(2)
        head.append(ListNode(4)).append(ListNode(3))

        list_val = 342
        self.assertEqual(list_val, get_list_value(head))

    def test_list2(self):
        head = ListNode(0)

        list_val = 0
        self.assertEqual(list_val, get_list_value(head))

    def test_list3(self):
        head = ListNode(3)

        list_val = 3
        self.assertEqual(list_val, get_list_value(head))

    def test_list4(self):
        head = ListNode(3)
        head.append(ListNode(9))

        list_val = 93
        self.assertEqual(list_val, get_list_value(head))

    def test_list5(self):
        head = ListNode(5)
        head.append(ListNode(6)).append(ListNode(4))

        list_val = 465
        self.assertEqual(list_val, get_list_value(head))

    def test_box_into_list1(self):
        t = 465
        head = ListNode(5)
        head.append(ListNode(6)).append(ListNode(4))
        v1 = get_list_value(head)
        v2 = get_list_value(ListNode.box_into_list(t))
        self.assertEqual(v1, v2)

    def test_box_into_list2(self):
        t = 342
        head = ListNode(2)
        head.append(ListNode(4)).append(ListNode(3))
        v1 = get_list_value(head)
        v2 = get_list_value(ListNode.box_into_list(t))
        self.assertEqual(v1, v2)

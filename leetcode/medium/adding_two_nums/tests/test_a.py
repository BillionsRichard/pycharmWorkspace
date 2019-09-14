# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/1 11:08 
"""
import unittest
from medium.adding_two_nums.srcs.answer import Solution
from medium.adding_two_nums.srcs.answer import ListNode
from medium.adding_two_nums.srcs.answer import get_list_value

class TestAnaswer(unittest.TestCase):
    def setUp(self):
        print('setting up')

    def tearDown(self):
        print('tearing down..')

    def test_solution1(self):
        h1 = ListNode(2)
        h1.append(ListNode(4)).append(ListNode(3))

        h2 = ListNode(5)
        h2.append(ListNode(6)).append(ListNode(4))

        s = Solution()
        sum_list = s.addTwoNumbers(h1, h2)
        real_list = ListNode.box_into_list(807)
        self.assertEqual(get_list_value(real_list),
                         get_list_value(sum_list))

    def test_solution2(self):
        h1 = ListNode(0)

        h2 = ListNode(5)
        h2.append(ListNode(6)).append(ListNode(4))

        s = Solution()
        sum_list = s.addTwoNumbers(h1, h2)
        real_list = ListNode.box_into_list(465)
        self.assertEqual(get_list_value(real_list),
                         get_list_value(sum_list))

    def test_solution3(self):
        h1 = ListNode(9)

        h2 = ListNode(5)
        h2.append(ListNode(6)).append(ListNode(4))

        s = Solution()
        sum_list = s.addTwoNumbers(h1, h2)
        real_list = ListNode.box_into_list(474)
        self.assertEqual(get_list_value(real_list),
                         get_list_value(sum_list))

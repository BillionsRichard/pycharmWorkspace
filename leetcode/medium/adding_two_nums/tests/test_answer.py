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


class TestAnaswer(unittest.TestCase):
    def setUp(self):
        print('setting up')

    def tearDown(self):
        print('tearing down..')

    def test_solution1(self):
        h1 = ListNode(2)
        node2 = ListNode(4)
        node3 = ListNode(3)
        h1.next = node2
        node2.next = node3

        h2 = ListNode(5)
        n2 = ListNode(6)
        n3 = ListNode(4)
        h2.next = n2
        n2.next = n3

        s = Solution()
        sum_list = s.addTwoNumbers(h1, h2)
        real_list = Solution.box_into_list(807)
        self.assertEqual(Solution.get_list_val(real_list),
                         Solution.get_list_val(sum_list))

    def test_solution2(self):
        h1 = ListNode(0)

        h2 = ListNode(5)
        h2.next = ListNode(6)
        h2.next.next = ListNode(4)
        
        s = Solution()
        sum_list = s.addTwoNumbers(h1, h2)
        real_list = Solution.box_into_list(465)
        self.assertEqual(Solution.get_list_val(real_list),
                         Solution.get_list_val(sum_list))

    def test_solution3(self):
        h1 = ListNode(9)

        h2 = ListNode(5)
        h2.next = ListNode(6)
        h2.next.next = ListNode(4)

        s = Solution()
        sum_list = s.addTwoNumbers(h1, h2)
        real_list = Solution.box_into_list(474)
        self.assertEqual(Solution.get_list_val(real_list),
                         Solution.get_list_val(sum_list))

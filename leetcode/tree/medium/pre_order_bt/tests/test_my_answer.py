# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 19:03 
"""
import unittest

from tree.medium.pre_order_bt.srcs.my_answer import Solution
from tree.medium.pre_order_bt.srcs.my_answer import TreeNode


class TestPreOrderBinaryTree(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        r = TreeNode(1)
        r.right = TreeNode(2)
        r.right.left = TreeNode(3)

        exp = [1, 2, 3]
        act = Solution().preorderTraversal(r)
        self.assertEqual(exp, act)

    def test_2(self):
        r = TreeNode(1)
        r.left = TreeNode(3)
        r.right = TreeNode(5)

        r.left.left = TreeNode(7)
        r.left.right = TreeNode(9)

        r.left.left.left = TreeNode(11)
        r.left.left.right = TreeNode(12)

        r.left.right = TreeNode(9)
        r.left.right.left = TreeNode(13)
        r.left.right.right = TreeNode(15)

        exp = [1, 3, 7, 11, 12, 9, 13, 15, 5]
        act = Solution().preorderTraversal(r)
        self.assertEqual(exp, act)

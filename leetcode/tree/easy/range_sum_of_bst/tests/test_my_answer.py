# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 14:43 
"""
from pprint import pprint as pp
from tree.easy.range_sum_of_bst.srcs.my_answer import TreeNode
from tree.easy.range_sum_of_bst.srcs.my_answer import Solution

import unittest


class TestRangeSumBST(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)

        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.right = TreeNode(18)

        exp = 32
        act = Solution().rangeSumBST(root, 7, 15)
        self.assertEqual(exp, act)

    def test_2(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)

        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(18)

        root.left.left.left = TreeNode(1)
        root.left.right.left = TreeNode(6)

        exp = 23
        act = Solution().rangeSumBST(root, 6, 10)
        self.assertEqual(exp, act)

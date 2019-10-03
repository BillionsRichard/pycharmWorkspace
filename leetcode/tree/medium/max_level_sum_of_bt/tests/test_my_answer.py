# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 20:53 
"""
from pprint import pprint as pp
from tree.medium.max_level_sum_of_bt.srcs.my_answer import TreeNode
from tree.medium.max_level_sum_of_bt.srcs.my_answer import Solution
import unittest


class TestMaxLevelSum(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        r = TreeNode(1)
        r.left = TreeNode(7)
        r.right = TreeNode(0)

        r.left.left = TreeNode(7)
        r.left.right = TreeNode(-8)

        s = Solution()
        exp = 2
        act = s.maxLevelSum(r)
        self.assertEqual(exp, act)

    def test_2(self):
        r = TreeNode(1)
        r.left = TreeNode(7)
        r.right = TreeNode(0)

        r.left.left = TreeNode(7)
        r.left.right = TreeNode(-8)

        r.right.left = TreeNode(7)

        s = Solution()
        exp = 2
        act = s.maxLevelSum(r)
        self.assertEqual(exp, act)

    def test_3(self):
        r = TreeNode(1)
        r.left = TreeNode(7)
        r.right = TreeNode(0)

        r.left.left = TreeNode(7)
        r.left.right = TreeNode(-8)

        r.right.left = TreeNode(8)

        print('level order traverse tree:', Solution.lvl_order_tree(r))
        s = Solution()
        exp = 2
        act = s.maxLevelSum(r)
        self.assertEqual(exp, act)

    def test_4(self):
        r = TreeNode(1)
        r.left = TreeNode(7)
        r.right = TreeNode(0)

        r.left.left = TreeNode(7)
        r.left.right = TreeNode(-8)

        r.right.left = TreeNode(9)
        print('level order traverse tree:', Solution.lvl_order_tree(r))

        s = Solution()
        exp = 3
        act = s.maxLevelSum(r)
        self.assertEqual(exp, act)

    def test_5(self):
        r = TreeNode(1)
        r.left = TreeNode(7)
        r.right = TreeNode(0)

        r.left.left = TreeNode(7)
        r.left.right = TreeNode(-8)

        r.right.left = TreeNode(9)
        r.right.left = TreeNode(9)
        r.right.left.left = TreeNode(9)
        print('level order traverse tree:', Solution.lvl_order_tree(r))

        s = Solution()
        exp = 4
        act = s.maxLevelSum(r)
        self.assertEqual(exp, act)

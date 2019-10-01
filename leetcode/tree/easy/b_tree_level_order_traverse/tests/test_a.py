# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/22 17:06 
"""
from tree.easy.b_tree_level_order_traverse.srcs.a import Solution
from tree.easy.b_tree_level_order_traverse.srcs.a import TreeNode
import unittest


class TestLevelOrderTraverseTree(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        r = TreeNode(3)
        l1 = TreeNode(9)
        r1 = TreeNode(20)
        r.left = l1
        r.right = r1

        r1.left = TreeNode(15)
        r1.right = TreeNode(7)

        s = Solution()
        exp = [
            [15, 7],
            [9, 20],
            [3]
        ]
        act = s.levelOrderBottom(r)

        self.assertEqual(exp, act)

    def test_2(self):
        r = None
        s = Solution()
        self.assertEqual([], s.levelOrderBottom(r))

    def test_3(self):
        r = TreeNode(1)
        r.left = TreeNode(2)
        r.right = TreeNode(3)

        right = r.right
        right.left = TreeNode(4)
        right.right = TreeNode(5)

        right = right.right
        right.left = TreeNode(6)
        right.right = TreeNode(7)

        right = right.right
        right.left = TreeNode(8)
        right.right = TreeNode(9)

        right = right.right
        right.right = TreeNode(10)
        right.right.right = TreeNode(11)

        s = Solution()
        exp = [
            [11],
            [10],
            [8, 9],
            [6, 7],
            [4, 5],
            [2, 3],
            [1],
        ]
        act = s.levelOrderBottom(r)
        self.assertEqual(exp, act)

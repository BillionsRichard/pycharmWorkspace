# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 15:29 
"""
import unittest

from tree.easy.merge_bt.srcs.my_answer import Solution
from tree.easy.merge_bt.srcs.my_answer import TreeNode


class TestMergeTrees(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_1(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(3)
        root1.right = TreeNode(2)

        root1.left.left = TreeNode(5)

        root2 = TreeNode(2)
        root2.left = TreeNode(1)
        root2.right = TreeNode(3)

        root2.left.right = TreeNode(4)
        root2.right.right = TreeNode(7)

        r = TreeNode(3)
        r.left= TreeNode(4)
        r.right= TreeNode(5)
        r.left.left = TreeNode(5)
        r.left.right = TreeNode(4)

        r.right.right = TreeNode(7)

        exp = Solution().mergeTrees(root1, root2)
        print('pre expect tree:', Solution.pre_order_bt(r))
        print('pre merged tree:', Solution.pre_order_bt(exp))
        self.assertTrue(Solution.is_tree_equal(r, exp))

    def test_2(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.left.left = TreeNode(3)

        root2 = TreeNode(1)
        root2.right = TreeNode(2)
        root2.right.right = TreeNode(3)

        r = TreeNode(2)
        r.left= TreeNode(2)
        r.right= TreeNode(2)
        r.left.left = TreeNode(3)
        r.right.right = TreeNode(3)

        exp = Solution().mergeTrees(root1, root2)
        print('pre expect tree:', Solution.pre_order_bt(r))
        print('pre merged tree:', Solution.pre_order_bt(exp))
        self.assertTrue(Solution.is_tree_equal(r, exp))
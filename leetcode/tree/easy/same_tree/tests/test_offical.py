# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/22 11:36 
"""
from pprint import pprint as pp
from tree.easy.same_tree.srcs.a_offical import Solution
from tree.easy.same_tree.srcs.a_offical import TreeNode
import unittest

class TestIsSameTree(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_1(self):
        p = TreeNode(1)
        l1 = TreeNode(2)
        r1 = TreeNode(3)
        p.left = l1
        p.right = r1

        q = TreeNode(1)
        l2 = TreeNode(2)
        r2 = TreeNode(3)
        q.left = l2
        q.right = r2

        s = Solution()
        self.assertTrue(s.isSameTree(p, q))

    def test_2(self):
        p = TreeNode(1)
        l1 = TreeNode(2)
        p.left = l1

        q = TreeNode(1)
        r2 = TreeNode(2)
        q.right = r2

        s = Solution()
        self.assertFalse(s.isSameTree(p, q))


    def test_3(self):
        p = TreeNode(1)
        l1 = TreeNode(2)
        r1 = TreeNode(1)
        p.left = l1
        p.right = r1

        q = TreeNode(1)
        l2 = TreeNode(1)
        r2 = TreeNode(2)
        q.left = l2
        q.right = r2

        s = Solution()
        self.assertFalse(s.isSameTree(p, q))



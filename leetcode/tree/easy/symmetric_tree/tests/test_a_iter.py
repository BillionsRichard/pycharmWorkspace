# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/22 12:23 
"""
from tree.easy.symmetric_tree.srcs.a_iter import Solution
from tree.easy.symmetric_tree.srcs.a import TreeNode
import unittest


class TestIsSymmetricTree(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        r = TreeNode(1)
        l1 = TreeNode(2)
        r1 = TreeNode(2)
        r.left = l1
        r.right = r1

        l1.left = TreeNode(3)
        l1.right = TreeNode(4)
        r1.left = TreeNode(4)
        r1.right = TreeNode(3)

        s = Solution()
        self.assertTrue(s.isSymmetric(r))

    def test_2(self):
        r = TreeNode(1)
        l1 = TreeNode(2)
        r1 = TreeNode(2)
        r.left = l1
        r.right = r1

        l1.right = TreeNode(3)
        r1.right = TreeNode(3)

        s = Solution()
        self.assertFalse(s.isSymmetric(r))

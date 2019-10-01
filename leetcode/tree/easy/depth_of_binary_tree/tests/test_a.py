# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/22 16:37 
"""

import unittest

from tree.easy.depth_of_binary_tree.srcs.a import Solution
from tree.easy.depth_of_binary_tree.srcs.a import TreeNode


class TestDepthOfBinayTree(unittest.TestCase):
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
        self.assertEqual(3, s.maxDepth(r))

    def test_2(self):
        r = None
        s = Solution()
        self.assertEqual(0, s.maxDepth(r))



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
        act = s.maxDepth(r)
        self.assertEqual(7, act)




# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/28 7:46 
"""
from pprint import pprint as pp
import unittest
from tree.easy.sorted_array_to_bst.srcs.my_answer import TreeNode
from tree.easy.sorted_array_to_bst.srcs.my_answer import Solution


class TestSortedArrayToBst(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        sa = [-10, -3, 0, 5, 9]
        """
        [0,-3,9,-10,null,5]
        """
        r = TreeNode(0)
        r.left = TreeNode(-3)
        r.right = TreeNode(9)

        r.left.left = TreeNode(-10)
        r.right.left = TreeNode(5)
        s = Solution()
        act = s.sortedArrayToBST(sa)

        print('exp tree:', s.in_order_traverse_tree(r))
        print('act tree:', s.in_order_traverse_tree(act))

        self.assertEqual(s.in_order_traverse_tree(r),
                         s.in_order_traverse_tree(act))

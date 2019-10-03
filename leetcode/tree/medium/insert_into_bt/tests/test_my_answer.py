# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 19:49 
"""
from pprint import pprint as pp
import unittest
from tree.medium.insert_into_bt.srcs.my_answer import TreeNode
from tree.medium.insert_into_bt.srcs.my_answer import Solution


class TestInsertIntoBinaryTree(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        r = TreeNode(4)
        r.left = TreeNode(2)
        r.right = TreeNode(7)
        r.left.left = TreeNode(1)
        r.left.right = TreeNode(3)

        insert_val = 5
        exp_in_order_traverse_ret = [1, 2, 3, 4, 5, 7]

        act_tree = Solution().insertIntoBST(r, insert_val)
        act_in_order_traverse_ret = Solution.in_order_traverse_tree(act_tree)
        self.assertEqual(exp_in_order_traverse_ret, act_in_order_traverse_ret)

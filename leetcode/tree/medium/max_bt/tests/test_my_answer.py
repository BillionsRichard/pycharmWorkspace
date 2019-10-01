# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 17:44 
"""
import unittest

from tree.medium.max_bt.srcs.my_answer import Solution
from tree.medium.max_bt.srcs.my_answer import TreeNode


class TestMaxBtree(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        nums = [3, 2, 1, 6, 0, 5]
        r = TreeNode(6)
        r.left = TreeNode(3)
        r.left.right = TreeNode(2)
        r.left.right.right = TreeNode(1)

        r.right = TreeNode(5)
        r.right.left = TreeNode(0)

        act = Solution().constructMaximumBinaryTree(nums)

        exp_post_order_list = Solution.post_order_traverse_tree(r)
        act_post_order_list = Solution.post_order_traverse_tree(act)
        print('exp_post_order_list', exp_post_order_list)
        print('act_post_order_list', act_post_order_list)

        self.assertTrue(exp_post_order_list,
                        act_post_order_list)
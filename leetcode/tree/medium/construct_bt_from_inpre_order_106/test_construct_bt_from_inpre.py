# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/11/10 10:48 
"""
import unittest

from tree.medium.construct_bt_from_inpre_order_106 \
    .construct_bt_from_inpre_order_106 import Solution
from tree.medium.construct_bt_from_inpre_order_106 \
    .construct_bt_from_inpre_order_106 import TreeNode
from utils.tree.btree_utils import TreeUtils as TU


class TestConstructBtFromInPre(unittest.TestCase):
    def setUp(self): pass

    def tearDown(self): pass

    def test_1(self):
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]
        act_bt = Solution().buildTree(inorder, postorder)

        r = TreeNode(3)
        r.left = TreeNode(9)
        r.right = TreeNode(20)
        r.right.left = TreeNode(15)
        r.right.right = TreeNode(7)

        self.assertTrue(TU.is_equal_trees(r, act_bt))

    def test_2(self):
        inorder = []
        postorder = [9, 15, 7, 20, 3]
        act_bt = Solution().buildTree(inorder, postorder)

        self.assertTrue(TU.is_equal_trees(None, act_bt))

    def test_3(self):
        postorder = []
        inorder = [9, 15, 7, 20, 3]
        act_bt = Solution().buildTree(inorder, postorder)

        self.assertTrue(TU.is_equal_trees(None, act_bt))

    def test_4(self):
        postorder = [1]
        inorder = [1]
        act_bt = Solution().buildTree(inorder, postorder)

        exp_tree = TreeNode(1)

        self.assertTrue(TU.is_equal_trees(exp_tree, act_bt))

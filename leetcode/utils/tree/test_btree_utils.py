# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/11/10 11:13 
"""
import unittest

from utils.tree.btree_utils import TreeUtils as TU
from utils.tree.btree_node import TreeNode


class TestTree(unittest.TestCase):
    def setUp(self): pass

    def tearDown(self): pass

    def test_traverse_1(self):
        r = TreeNode(0)
        pre_order, in_order, post_order = [0], [0], [0]
        act_pre, act_in, act_post = TU.pre_order(r), TU.in_order_iter(
            r), TU.post_order(r)

        self.assertEqual(pre_order, act_pre)
        self.assertEqual(in_order, act_in)
        self.assertEqual(post_order, act_post)

    def test_traverse_2(self):
        r = TreeNode(0)
        r.left = TreeNode(1)
        pre_order, in_order, post_order = [0, 1], [1, 0], [1, 0]
        act_pre, act_in, act_post = TU.pre_order(r), TU.in_order_iter(r), \
                                    TU.post_order(r)

        self.assertEqual(pre_order, act_pre)
        self.assertEqual(in_order, act_in)
        self.assertEqual(post_order, act_post)

    def test_traverse_3(self):
        r = TreeNode(0)
        r.right = TreeNode(1)
        pre_order, in_order, post_order = [0, 1], [0, 1], [1, 0]
        act_pre, act_in, act_post = TU.pre_order(r), TU.in_order_iter(
            r), TU.post_order(r)

        self.assertEqual(pre_order, act_pre)
        self.assertEqual(in_order, act_in)
        self.assertEqual(post_order, act_post)

    def test_traverse_4(self):
        r = TreeNode(0)
        r.left = TreeNode(1)
        r.right = TreeNode(2)

        pre_order, in_order, post_order = [0, 1, 2], [1, 0, 2], [1, 2, 0]
        act_pre, act_in, act_post = TU.pre_order(r), TU.in_order_iter(
            r), TU.post_order(r)

        self.assertEqual(pre_order, act_pre)
        self.assertEqual(in_order, act_in)
        self.assertEqual(post_order, act_post)

    def test_traverse_5(self):
        r = TreeNode(0)
        r.left = TreeNode(1)
        r.right = TreeNode(2)

        r.left.left = TreeNode(3)
        r.left.right = TreeNode(4)

        r.right.right = TreeNode(6)

        pre_order, in_order, post_order = ([0, 1, 3, 4, 2, 6],
                                           [3, 1, 4, 0, 2, 6],
                                           [3, 4, 1, 6, 2, 0])
        act_pre, act_in, act_post = TU.pre_order(r), TU.in_order_iter(
            r), TU.post_order(r)

        self.assertEqual(pre_order, act_pre)
        self.assertEqual(in_order, act_in)
        self.assertEqual(post_order, act_post)

    def test_traverse_6(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)

        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.left.left.right = TreeNode(5)

        root.right.right = TreeNode(6)
        root.right.right.left = TreeNode(7)

        pre_order, in_order, post_order = ([0, 1, 3, 5, 4, 2, 6, 7],
                                           [3, 5, 1, 4, 0, 2, 7, 6],
                                           [5, 3, 4, 1, 7, 6, 2, 0])
        act_pre, act_in, act_post = \
            TU.pre_order(root), TU.in_order_iter(root), TU.post_order(root)

        self.assertEqual(pre_order, act_pre)
        self.assertEqual(in_order, act_in)
        self.assertEqual(post_order, act_post)

    def test_equal_0(self):
        root1 = TreeNode(0)
        root2 = None
        self.assertFalse(TU.is_equal_trees(root1, root2))

    def test_equal_1(self):
        root1 = TreeNode(0)
        self.assertTrue(TU.is_equal_trees(root1, root1))

    def test_equal_2(self):
        r1 = TreeNode(0)
        r2 = TreeNode(0)
        self.assertTrue(TU.is_equal_trees(r1, r2))

    def test_equal_3(self):
        r1 = TreeNode(0)
        r1.left = TreeNode(1)
        r1.right = TreeNode(2)

        r2 = TreeNode(0)
        r2.left = TreeNode(1)
        r2.right = TreeNode(2)

        self.assertTrue(TU.is_equal_trees(r1, r2))

    def test_equal_4(self):
        r1 = TreeNode(0)
        r1.left = TreeNode(1)
        r1.right = TreeNode(2)

        r2 = TreeNode(0)
        r2.left = TreeNode(1)
        r2.right = TreeNode(1)

        self.assertFalse(TU.is_equal_trees(r1, r2))

    def test_equal_5(self):
        r1 = TreeNode(0)
        r1.left = TreeNode(1)
        r1.right = TreeNode(2)
        r1.left.left = TreeNode(3)
        r1.right.right = TreeNode(0)

        r2 = TreeNode(0)
        r2.left = TreeNode(1)
        r2.left.left = TreeNode(3)
        r2.right = TreeNode(2)
        r2.right.right = TreeNode(0)

        self.assertTrue(TU.is_equal_trees(r1, r2))

    def test_btree_lvl_order_1(self):
        r1 = None
        exp = []
        act = TU.lvl_order(r1)
        self.assertEqual(exp, act)

    def test_btree_lvl_order_2(self):
        r1 = TreeNode(0)

        exp = [0]
        act = TU.lvl_order(r1)
        self.assertEqual(exp, act)

    def test_btree_lvl_order_3(self):
        r1 = TreeNode(0)
        r1.left = TreeNode(1)

        exp = [0, 1]
        act = TU.lvl_order(r1)
        self.assertEqual(exp, act)

    def test_btree_lvl_order_4(self):
        r1 = TreeNode(0)
        r1.right = TreeNode(1)

        exp = [0, 1]
        act = TU.lvl_order(r1)
        self.assertEqual(exp, act)

    def test_btree_lvl_order_5(self):
        r1 = TreeNode(0)
        r1.left = TreeNode(1)
        r1.right = TreeNode(2)

        exp = [0, 1, 2]
        act = TU.lvl_order(r1)
        self.assertEqual(exp, act)

    def test_btree_lvl_order_6(self):
        r1 = TreeNode(0)
        r1.left = TreeNode(1)
        r1.right = TreeNode(2)

        r1.left.left = TreeNode(3)
        r1.left.left.right = TreeNode(4)

        r1.right.left = TreeNode(5)

        exp = [0, 1, 2, 3, 5, 4]
        act = TU.lvl_order(r1)
        self.assertEqual(exp, act)

    def test_btree_lvl_order_7(self):
        r1 = TreeNode(0)
        r1.left = TreeNode(1)
        r1.right = TreeNode(2)

        r1.left.left = TreeNode(3)
        r1.left.right = TreeNode(5)
        r1.left.left.right = TreeNode(7)

        r1.right.right = TreeNode(4)
        r1.right.right.left = TreeNode(8)

        exp = [0, 1, 2, 3, 5, 4, 7, 8]
        act = TU.lvl_order(r1)
        self.assertEqual(exp, act)

    def test_btree_to_string_8(self):
        r1 = TreeNode(0)
        r1.left = TreeNode(1)
        r1.right = TreeNode(2)

        r1.left.left = TreeNode(3)
        r1.left.right = TreeNode(5)
        r1.left.left.right = TreeNode(7)

        r1.right.right = TreeNode(4)
        r1.right.right.left = TreeNode(8)

        act = TU.to_string(r1)
        print(act)

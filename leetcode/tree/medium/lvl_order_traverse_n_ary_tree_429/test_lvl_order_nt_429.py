# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/11/10 16:41 
"""
import unittest
from tree.medium.lvl_order_traverse_n_ary_tree_429 \
    .lvl_order_traverse_ntree_429 import Solution
from tree.medium.lvl_order_traverse_n_ary_tree_429 \
    .lvl_order_traverse_ntree_429 import Node


class TestLvlOrderNTree(unittest.TestCase):
    def setUp(self): pass

    def tearDown(self): pass

    def test_1(self):
        c1 = Node(3, [Node(5, []), Node(6, [])])
        c2 = Node(2, [])
        c3 = Node(4, [])

        r = Node(1, [c1, c2, c3])
        exp = [
            [1],
            [3, 2, 4],
            [5, 6]
        ]
        act = Solution().levelOrder(r)
        self.assertEqual(exp, act)

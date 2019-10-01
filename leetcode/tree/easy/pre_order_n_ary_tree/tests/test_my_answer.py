# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 17:10 
"""
from pprint import pprint as pp

import unittest
from tree.easy.pre_order_n_ary_tree.srcs.my_answer import Solution
from tree.easy.pre_order_n_ary_tree.srcs.my_answer import Node

class TestPreorderNaryTree(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        left = Node(3, [Node(5), Node(6)])
        middle = Node(2)
        right = Node(4)
        children = [left, middle, right]
        root = Node(1, children)

        exp = [1,3,5,6, 2, 4]
        act = Solution().preorder(root)
        self.assertTrue(exp == act)




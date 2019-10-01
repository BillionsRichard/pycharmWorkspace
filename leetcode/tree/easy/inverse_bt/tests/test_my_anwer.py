# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 16:31 
"""
from pprint import pprint as pp
from tree.easy.inverse_bt.srcs.my_answer import TreeNode
from tree.easy.inverse_bt.srcs.my_answer import Solution
import unittest

class TestInverseBinaryTree(unittest.TestCase):
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

        r.right.left = TreeNode(6)
        r.right.right = TreeNode(9)

        exp = TreeNode(4)
        exp.left = TreeNode(7)
        exp.right = TreeNode(2)

        exp.left.left = TreeNode(9)
        exp.left.right = TreeNode(6)

        exp.right.left =TreeNode(3)
        exp.right.right = TreeNode(1)

        act = Solution().invertTree(r)

        print('pre order origin tree', Solution.pre_order_bt(r))
        print('pre order expted tree', Solution.pre_order_bt(exp))
        print('pre order inverted tree', Solution.pre_order_bt(act))




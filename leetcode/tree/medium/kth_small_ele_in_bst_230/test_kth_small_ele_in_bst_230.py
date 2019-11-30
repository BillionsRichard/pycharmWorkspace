# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/11/30 21:17
"""

from tree.medium.kth_small_ele_in_bst_230.kth_small_ele_in_bst_230 import \
    Solution
from tree.medium.kth_small_ele_in_bst_230.kth_small_ele_in_bst_230 import \
    TreeNode
import unittest


class TestKthSmallElementInBst(unittest.TestCase):
    def setUp(self): pass

    def tearDown(self): pass

    def test_1(self):
        """
        输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:
"""
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)

        root.left.right = TreeNode(2)
        k = 1
        exp = 1
        act = Solution().kthSmallest(root, k)
        self.assertEqual(exp, act)

    def test_2(self):
        """
        输入: root = [5,3,6,2,4,null,null,1], k = 3
               5
              / \
             3   6
            / \
           2   4
          /
         1
        输出: 3
        :return:
        """
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right  = TreeNode(6)

        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(1)
        k = 3
        exp = 3
        act = Solution().kthSmallest(root, k)
        self.assertEqual(exp, act)

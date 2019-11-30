# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/11/30 21:02
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def in_order_traverse(node: TreeNode, vals: List[int], k: -1):
            if not node:
                return

            if k > 0 and len(vals) >= k:
                return

            in_order_traverse(node.left, vals, k)
            vals.append(node.val)
            in_order_traverse(node.right, vals, k)

        vals = []
        in_order_traverse(root, vals, k)

        return vals[k - 1]

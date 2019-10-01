# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/22 17:05 
"""
"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在
的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from pprint import pprint as pp


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if root is None:
            return []

        vals = []
        Solution.BFS([root], vals)
        pp(vals)
        return vals

    @staticmethod
    def BFS(lvl_nodes, val_list):
        next_lvl_nodes = []
        this_lvl_vals = []
        for node in lvl_nodes:
            if node:
                this_lvl_vals.append(node.val)
                next_lvl_nodes.append(node.left)
                next_lvl_nodes.append(node.right)

        if this_lvl_vals:
            val_list.insert(0, this_lvl_vals)
        if next_lvl_nodes:
            Solution.BFS(next_lvl_nodes, val_list)

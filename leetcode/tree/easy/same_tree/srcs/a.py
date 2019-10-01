# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/22 11:11 
"""

"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

https://leetcode-cn.com/problems/same-tree/


自己的解题思路：
采用中序遍历法：将遍历结果放在列表中，
为空的节点存None进行占位。

比较两棵树的遍历结果是否相等（两个列表进行比较）

"""
from pprint import pprint as pp


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_val_list = []
        q_val_list = []
        Solution.pre_order_traverse(p, p_val_list)
        Solution.pre_order_traverse(q, q_val_list)

        print('p--->', p_val_list)
        print('q--->', q_val_list)
        return p_val_list == q_val_list

    @staticmethod
    def pre_order_traverse(root: TreeNode, node_val_list):
        if not root:
            node_val_list.append(None)
            return

        node_val_list.append(root.val)
        Solution.pre_order_traverse(root.left, node_val_list)
        Solution.pre_order_traverse(root.right, node_val_list)

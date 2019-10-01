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


官方解题思路：递归算法

1、比较两棵树的根节点是否相同。
    比较根节点是否相同的算法：
    1）根节点是否都为空，如果是则返回True
    2）根节点其中一个为空，则不相等，返回False
    3）根节点值不相等，则不相等；返回False
    
    4）对左右子树运用 1）~ 3）的算法 递归 比较左子树和右子树是否相等。
    
2、比较左子树和右子树是否相同。

"""
from pprint import pprint as pp


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))

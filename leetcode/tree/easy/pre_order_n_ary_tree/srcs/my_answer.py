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
"""
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :

 



 

返回其前序遍历: [1,3,5,6,2,4]。

 

说明: 递归法很简单，你可以使用迭代法完成此题吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from pprint import pprint as pp


# Definition for a Node.
class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> list:
        if not root:
            return None

        if not root.children:
            return [root.val]

        vals = [root.val]
        for child in root.children:
            child_vals = self.preorder(child)
            vals.extend(child_vals)

        return vals

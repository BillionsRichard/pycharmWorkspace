# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 19:02 
"""
"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        """递归实现先序遍历。

        :param root:
        :return:
        """
        if not root:
            return []

        vals = [root.val]
        vals.extend(self.preorderTraversal(root.left))
        vals.extend(self.preorderTraversal(root.right))
        return vals

    def preorderTraversal_iter(self, root: TreeNode) -> list:
        """迭代法实现先序遍历。

        :param root:
        :return:
        """
        if not root:
            return []

        vals = [root.val]
        tmp_list = [root.left, root.right]

        while tmp_list:
            node = tmp_list.pop(0)
            if node:
                vals.append(node.val)
                if node.right:
                    tmp_list.insert(0, node.right)

                if node.left:
                    tmp_list.insert(0, node.left)

        return vals

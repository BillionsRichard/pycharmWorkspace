# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/11/10 10:20 
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None

        """
        中序遍历 inorder = [9,3,15,20,7]
        后序遍历 postorder = [9,15,7,20,3]
        
        后序：左子树 -> 右子树 -> 根
        中序：左子树 -> 根 -> 右子树
        
        
            3
           / \
          9  20
            /  \
           15   7
        
        """
        root_val = postorder[-1]
        root = TreeNode(root_val)
        root_index_of_in_order = inorder.index(root_val)
        left_in_order = inorder[:root_index_of_in_order]
        right_in_order = inorder[root_index_of_in_order+1:]
        if not left_in_order:
            right_post_order = postorder[:-1]
            root.right = self.buildTree(right_in_order, right_post_order)
            return root
        elif not right_in_order:
            left_post_order = postorder[:-1]
            root.left = self.buildTree(left_in_order, left_post_order)
            return root

        for i in range(len(postorder)):
            if postorder[i] not in left_in_order:
                break

        left_post_order = postorder[:i]
        right_post_order = postorder[i:-1]
        root.left = self.buildTree(left_in_order, left_post_order)
        root.right = self.buildTree(right_in_order, right_post_order)
        return root






# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 19:49 
"""

"""
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉
搜索树的根节点。 保证原始二叉搜索树中不存在新值。

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回
任意有效的结果。

例如, 

给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和 插入的值: 5
你可以返回这个二叉搜索树:

         4
       /   \
      2     7
     / \   /
    1   3 5
或者这个树也是有效的:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-into-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root

        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
                return root
            else:
                root.left = self.insertIntoBST(root.left, val)
                return root

        if root.right is None:
            root.right = TreeNode(val)
            return root

        root.right = self.insertIntoBST(root.right, val)
        return root

    @staticmethod
    def in_order_traverse_tree(root: TreeNode):
        if not root:
            return []

        vals = Solution().in_order_traverse_tree(root.left)
        vals.append(root.val)
        vals.extend(Solution().in_order_traverse_tree(root.right))
        return vals

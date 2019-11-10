# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/11/10 10:52 
"""
from utils.tree.tree_node import TreeNode


class TreeUtils(object):
    def __init__(self, root: TreeNode):
        self.root = root

    @staticmethod
    def in_order(root: TreeNode) -> list:
        if not root:
            return []

        in_order_vals = []
        in_order_vals.extend(TreeUtils.in_order(root.left))
        in_order_vals.append(root.val)
        in_order_vals.extend(TreeUtils.in_order(root.right))
        return in_order_vals

    @staticmethod
    def pre_order(root: TreeNode):
        if not root:
            return []

        pre_order_vals = [root.val]
        pre_order_vals.extend(TreeUtils.pre_order(root.left))
        pre_order_vals.extend(TreeUtils.pre_order(root.right))
        return pre_order_vals

    @staticmethod
    def post_order(root):
        if not root:
            return []

        post_order_vals = []
        post_order_vals.extend(TreeUtils.post_order(root.left))
        post_order_vals.extend(TreeUtils.post_order(root.right))
        post_order_vals.append(root.val)
        return post_order_vals

    @staticmethod
    def to_string(root: TreeNode):
        if not root:
            return 'Empty tree'

        return 'In order:{}\nPre order:{}\nPost order:{}'.format(
            TreeUtils.in_order(root),
            TreeUtils.pre_order(root),
            TreeUtils.post_order(root)
        )

    @staticmethod
    def is_equal_trees(root1: TreeNode, root2: TreeNode):
        if not root1 and not root2:
            return True

        if root1 is None or root2 is None:
            return False

        if root1 is root2:
            return True

        return (root1.val == root2.val
                and TreeUtils.is_equal_trees(root1.left, root2.left)
                and TreeUtils.is_equal_trees(root1.right, root2.right)
                )

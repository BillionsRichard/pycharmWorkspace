# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/28 7:46 
"""
from pprint import pprint as pp


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """有序数组转换成平衡二叉搜索树。采用二分查找递归创建左右子树的思路。
    和官方题解一直：

    https://leetcode-cn.com/problems/convert-sorted-num_array-to-binary-search-tree/
    """

    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if not nums:
            return None

        middle = len(nums) // 2
        r_val = nums[middle]
        r = TreeNode(r_val)
        r.left = self.sortedArrayToBST(nums[:middle])
        r.right = self.sortedArrayToBST(nums[middle + 1:])
        return r

    def in_order_traverse_tree(self, root: TreeNode) -> list:
        """树的中序遍历法，递归思路：
        1、先遍历左子树，再遍历根节点，然后是右子树。
        2、针对左右子树的遍历采用同样的思路。


        :param root:
        :return:
        """
        if not root:
            return []

        vals = []
        left_vals = self.in_order_traverse_tree(root.left)
        right_vals = self.in_order_traverse_tree(root.right)

        vals.extend(left_vals)
        vals.append(root.val)
        vals.extend(right_vals)

        return vals

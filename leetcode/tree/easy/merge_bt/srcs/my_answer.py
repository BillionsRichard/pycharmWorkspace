# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 15:29 
"""
"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重
叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加
作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
输出: 
合并后的树:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
注意: 合并必须从两个树的根节点开始。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """二叉树的合并，递归算法。

        :param t1:
        :param t2:
        :return:
        """
        if t1 is None and t2 is None:
            return None

        if t1 is None:
            return t2

        if t2 is None:
            return t1

        root = TreeNode(t1.val + t2.val)

        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root

    @staticmethod
    def pre_order_bt(root: TreeNode):
        if not root:
            return []

        vals = [root.val]
        vals.extend(Solution.pre_order_bt(root.left))
        vals.extend(Solution.pre_order_bt(root.right))
        return vals

    @staticmethod
    def is_tree_equal(this: TreeNode, other: TreeNode):
        return Solution().pre_order_bt(this) == Solution.pre_order_bt(
            other)

# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 20:53 
"""
"""
给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 
层，依此类推。

请你找出层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。

 

示例：



输入：[1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。
 

提示：

树中的节点数介于 1 和 10^4 之间
-10^5 <= node.val <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-level-sum-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        lvl = 1
        max_sum = root.val
        max_lvl = 1
        lvl_nodes = [root.left, root.right]
        while lvl_nodes:
            lvl += 1
            lvl_sum = 0
            children = []
            for lvl_node in lvl_nodes:
                if lvl_node:
                    lvl_sum += lvl_node.val
                    children.append(lvl_node.left)
                    children.append(lvl_node.right)

            if lvl_sum > max_sum:
                max_sum = lvl_sum
                max_lvl = lvl

            lvl_nodes = children

        return max_lvl

    @staticmethod
    def lvl_order_tree(root: TreeNode):
        if not root:
            return []

        vals = [root.val]
        lvl_nodes = [root.left, root.right]

        while lvl_nodes:
            children = []
            for lvl_node in lvl_nodes:
                if lvl_node:
                    vals.append(lvl_node.val)
                    if lvl_node.left:
                        children.append(lvl_node.left)
                    if lvl_node.right:
                        children.append(lvl_node.right)

            lvl_nodes = children
        return vals

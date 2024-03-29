# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 16:30 
"""
"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出
翻转二叉树这道题，这太糟糕了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        root.left,root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    @staticmethod
    def pre_order_bt(root:TreeNode, ret_list=None):
        if not root:
            return []

        if not ret_list:
            ret_list = [root.val]
        else:
            ret_list.append(root.val)

        ret_list.extend(Solution.pre_order_bt(root.left))
        ret_list.extend(Solution.pre_order_bt(root.right))
        return ret_list


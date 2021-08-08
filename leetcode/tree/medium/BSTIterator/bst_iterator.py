# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/11/29 18:10
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.in_order_list = self._in_order_traverse(root)

        self.len = len(self.in_order_list)
        self.cur = 0


    def _in_order_traverse(self, root):
        if not root:
            return []

        in_order_vals = []
        left_eles = self._in_order_traverse(root.left)
        in_order_vals.extend(left_eles)

        in_order_vals.append(root.val)

        right_eles = self._in_order_traverse(root.right)
        in_order_vals.extend(right_eles)
        return in_order_vals


    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.cur >= self.len:
            raise StopIteration

        self.cur += 1
        return self.in_order_list[self.cur-1]



    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.cur < self.len



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
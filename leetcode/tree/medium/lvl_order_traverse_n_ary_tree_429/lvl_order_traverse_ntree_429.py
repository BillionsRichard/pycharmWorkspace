# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/11/10 16:31 
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        lvl = 1
        queue = [(lvl, root)]
        ans = []

        while queue:
            depth, node = queue.pop(0)
            if node:
                if len(ans) < depth:
                    ans.append([node.val])
                else:
                    ans[depth - 1].append(node.val)

                for child in node.children:
                    queue.append((depth + 1, child))

        return ans

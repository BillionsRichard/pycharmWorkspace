# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/11/10 10:50 
"""


class TreeNode(object):
    def __init__(self, val,
                 left: 'TreeNode ' = None,
                 right: 'TreeNode ' = None):
        self.val = val
        self.left = left
        self.right = right


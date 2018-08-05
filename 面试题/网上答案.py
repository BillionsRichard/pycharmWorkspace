# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 网上答案.py 
@time: 2018/7/26 22:03 
"""
from pprint import pprint as P


class node():
    def __init__(self, k=None, l=None, r=None):
        self.val = k
        self.left = l
        self.right = r


def listcreattree(root, llist, i):  ###用列表递归创建二叉树，
    # 它其实创建过程也是从根开始a开始，创左子树b，再创b的左子树，如果b的左子树为空，返回none。
    # 再接着创建b的右子树，
    if i < len(llist):
        if llist[i] is None:
            return None  ###这里的return很重要
        else:
            root = node(k=llist[i])
            print(i)
            root.left = listcreattree(root.left, llist, 2 * i + 1)
            root.right = listcreattree(root.right, llist, 2 * i + 2)
            return root  ###这里的return很重要
    return root


if __name__ == '__main__':
    root = node()
    llist = ['1', '2', '3', None, '4', '5', '7', '9']
    root = listcreattree(root, llist, 0)

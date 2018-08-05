# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: None
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 二叉树的实现.py 
@time: 2018/7/26 20:24 
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None


def create_tree(root, item_list, i):
    """用列表递归创建二叉树，

    :param root:
    :param item_list:
    :param i:
    :return:
    """
    if not item_list:
        return None

    if i < len(item_list):
        if item_list[i] is None:
            return None
        else:
            root = Node(item_list[i])
            root.left_child = create_tree(root.left_child, item_list, 2 * i + 1)
            root.right_child = create_tree(root.right_child, item_list, 2 * i + 2)
            return root

    return root


def pre_order_traverse(root):
    """先序遍历

    :return:
    """
    if root is None:
        return

    print(root.item)
    pre_order_traverse(root.left_child)
    pre_order_traverse(root.right_child)


def in_order_traverse(root):
    """中序遍历

    :param root:
    :return:
    """
    if root is None:
        return

    in_order_traverse(root.left_child)
    print(root.item)
    in_order_traverse(root.right_child)


def post_order_traverse(root):
    """后续遍历

    :return:
    """
    if root is None:
        return

    post_order_traverse(root.left_child)
    post_order_traverse(root.right_child)
    print(root.item)


if __name__ == '__main__':
    root = Node('root')
    create_tree(root, ['A', 'B', 'C', None, 'D', 'E'], 0)
    pre_order_traverse(root)

# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 递归与堆栈的应用-汉诺塔游戏.py 
@time: 2018/8/5 15:40 
"""
from pprint import pprint as P


def hanoi(n, p1, p2, p3):
    """汉诺塔游戏，移动的次数为2^1 -1 次。

    :param n:
    :param p1:
    :param p2:
    :param p3:
    :return:
    """
    step_list = []
    if n == 1:
        step = (p1, p3)
        step_list.append(step)
    else:
        step_list.extend(hanoi(n - 1, p1, p3, p2))  # 将n-1个盘子从p1移动到p2
        # print('%s--->%s' % (p1, p3))  # 将第n个盘子从p1,移动到P3
        step = (p1, p3)
        step_list.append(step)
        step_list.extend(hanoi(n - 1, p2, p1, p3))  # 将n-1个盘子从p2移动到p3
    return step_list


if __name__ == '__main__':
    n = eval(input("请输入盘子个数:"))
    step_list = hanoi(n, 1, 2, 3)
    P(step_list)
    print(len(step_list))
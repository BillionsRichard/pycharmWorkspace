# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: selectSorting.py 
@time: 2018/8/8 7:03 
"""
from pprint import pprint as P


def select_sorting(in_list):
    if not in_list:
        return in_list

    length = len(in_list)
    for i in range(length - 1, 0, -1):  # range(start, end, -1)不包含end
        idx = 0
        for j in range(i):
            if in_list[j] > in_list[idx]:
                idx = j

        if in_list[i] < in_list[idx]:
            in_list[i], in_list[idx] = in_list[idx], in_list[i]

        print('第%s次结果:%s' % (i, str(in_list)))
    return in_list


if __name__ == '__main__':
    print(select_sorting([2, 9, 8, 7, 5, 3, 1, -1]))
    print(select_sorting([4, 2, 9, 8, 7, 5, 3, 1, 2]))

# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/20 10:11 
"""


def bsearch(target: int, l: list) -> int:
    """ 二分查找

    :param target:
    :param l:
    :return:
    """
    if not l:
        return -1

    low = 0
    hi = len(l) - 1
    while low <= hi:
        mid = low + (hi - low) // 2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            hi = mid - 1
        else:
            low = mid + 1
    return -1

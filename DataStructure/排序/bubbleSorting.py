# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: bubbleSorting.py 
@time: 2018/8/8 6:56 
"""
from pprint import pprint as P


def bubbleSorting(input_list):
    if not input_list:
        return input_list

    length = len(input_list)
    for i in range(length - 1, 1, -1):
        swapped = False
        for j in range(i):
            if input_list[i] < input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]
                swapped = True
        if not swapped:
            break
    return input_list


if __name__ == '__main__':
    print(bubbleSorting([2, 9, 8, 7, 5, 3, 1, -1]))

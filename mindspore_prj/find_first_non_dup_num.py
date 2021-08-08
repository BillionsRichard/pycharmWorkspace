# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/10/25 17:08
"""
from collections import defaultdict


def find_first_non_dup_num(input_nums):
    num_count_dict = defaultdict(int)
    for i in input_nums:
        num_count_dict[i] += 1

    for i in input_nums:
        if num_count_dict.get(i) == 1:
            return i


if __name__ == '__main__':
    l = [1, 1, 2, 3, 4, 5]
    print(find_first_non_dup_num(l))

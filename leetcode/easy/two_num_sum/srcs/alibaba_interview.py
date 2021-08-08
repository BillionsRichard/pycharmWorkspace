# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/12/12 21:11
"""

# // 评测题目: 无
#
# // 编程语言：c / c + +或者python
# // 输入：排序数组(array)，指定数字(sum)
# // 输出：如果有两个数字的和等于指定数字(sum)，返回1，否则返回0
#
# // [1, 2, 4, 5, 8]
# 10
# // 0: 9
# // 1: 8
# // 2: 6
# // 3: 5
# // 4: 2


def exist_two_nums_equals_sum(input_list, target_sum):
    if not input_list or len(input_list) < 2:
        return False

    remain_index_dict = dict()

    for i, num in enumerate(input_list):
        remain = target_sum - num
        remain_index_dict[remain] = i

    for i, num in enumerate(input_list):
        if num in remain_index_dict and i != remain_index_dict.get(num):
            return True

    return False


if __name__ == '__main__':
    l = [1, 2, 4, 5, 8]
    r = exist_two_nums_equals_sum(l, 8)
    print(r)

# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/1/12 16:03
"""
from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        from collections import defaultdict

        op_map = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }

        def dfs(step, res):
            if step == 3 and res == 24:
                return True

            for i in range(4):
                if not taken[i]:
                    next_num = nums[i]
                    taken[i] = True
                    for sign in ['+', '-', '*', '/']:
                        new_res = op_map.get(sign)(res, next_num)
                        if dfs(step + 1, new_res):
                            return True
                    taken[i] = False


        taken = defaultdict(bool)

        for j in range(4):
            taken.clear()
            taken[j] = True
            if dfs(0, nums[j]):
                return True
        return False

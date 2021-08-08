# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2021/1/10 10:25
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        start_end_pairs = []
        num_len = len(nums)
        i = 0
        while i < num_len:
            start = i
            pair = [str(nums[i]), ]
            while i < num_len - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1

            if i > start:
                pair.append(str(nums[i]))

            i += 1
            start_end_pairs.append(pair)

        return ['->'.join(pair) for pair in start_end_pairs]


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]

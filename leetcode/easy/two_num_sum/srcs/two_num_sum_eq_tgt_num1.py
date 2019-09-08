# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: two_num_sum_eq_tgt_num.py 
@time: 2019/8/25 18:28 
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_len = len(nums)
        for t1 in nums:
            t2 = target - t1
            if t2 not in nums:
                continue

            if t1 == t2:
                if nums.count(t1) == 1:
                    continue
                else:
                    return [i for i in range(num_len) if nums[i] == t1][:2]
            else:
                return [nums.index(t1), nums.index(t2)]

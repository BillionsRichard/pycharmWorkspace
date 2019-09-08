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
from pprint import pprint as pp
import itertools


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, j in itertools.combinations(nums, 2):
            if i + j == target:
                return [nums.index(i), nums.index(j)]
            else:
                first_indx = nums.index(i)
                second_indx = nums[first_indx + 1:].index(j) + len(nums[:first_indx+1])
                return [first_indx, second_indx]

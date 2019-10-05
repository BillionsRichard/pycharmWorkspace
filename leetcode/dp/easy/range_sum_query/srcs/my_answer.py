# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/4 15:09 
"""


class NumArray:

    def __init__(self, nums: list):
        self.nums = nums

        def calc_sum(nums):
            if not nums:
                return {0:0}
            sum_dic = {0: nums[0]}
            for i in range(1, len(nums)):
                sum_dic[i] = sum_dic[i-1] + nums[i]
            return sum_dic

        self.sum_dict = calc_sum(nums)

    def sumRange(self, i: int, j: int) -> int:
        return self.sum_dict.get(j, 0) - self.sum_dict.get(i - 1, 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

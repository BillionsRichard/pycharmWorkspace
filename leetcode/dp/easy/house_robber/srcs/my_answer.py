# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/4 17:07 
"""


class Solution:
    def rob(self, nums: list) -> int:
        if not nums:
            return 0

        num_len = len(nums)
        if num_len <= 2:
            return max(nums)

        dp = [nums[0], nums[1], nums[0] + nums[2]]
        for i in range(3, num_len):
            dp_i= max(dp[i-2], dp[i-3]) + nums[i]
            dp.append(dp_i)

        return max(dp[-1], dp[-2])

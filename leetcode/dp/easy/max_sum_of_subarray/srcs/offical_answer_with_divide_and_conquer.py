# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/5 8:03 
"""
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），
返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxSubArray(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        middle = n // 2
        # 情形 1：左半边的最大子序和 （不含中间元素）
        left_max = self.maxSubArray(nums[:middle])
        # 情形 2：右半边的最大子序和（含中间元素）
        right_max = self.maxSubArray(nums[middle:])

        # 分治关键点：3.1 不能包含中间元素，3.2包含中间元素，反之用例 2无法通过？
        # TODO： 为什么必须这样分？ 不理解！
        # 情形 3：中间部分的最大子序和 （必须包含 middle 左右两侧的元素）
        # 3.1 中间以左（不含中间元素）
        max_l = nums[middle - 1]
        left_sum = 0
        for i in range(middle - 1, -1, -1):
            left_sum += nums[i]
            max_l = max(left_sum, max_l)

        # 3.2 中间以右（含中间元素）
        max_r = nums[middle]
        right_sum = 0
        for i in range(middle, n):
            right_sum += nums[i]
            max_r = max(max_r, right_sum)

        middle_max = max_l + max_r
        return max(left_max, right_max, middle_max)

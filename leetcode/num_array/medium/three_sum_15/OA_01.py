# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/20 12:35 
"""


class Solution:
    """
    """

    def threeSum(self, nums: list) -> list:
        import sys
        nums = sorted(nums)
        res = []
        last = sys.maxsize
        for i in range(len(nums) - 2):

            if nums[i] != last:
                two_sum = -nums[i]

                for item in self.findTwosum(nums[i + 1:], two_sum):
                    res.append([nums[i]] + item)

                last = nums[i]

        return res

    def findTwosum(self, nums, two_sum):
        """ 在拍好序的数组 nums 中找两数 之和 等于 two_sum
        从两头向中间寻找。

        left + right == two_sum ?

        1) 等于， 则记录
        2） 小于： left+= 1
        3) 大于： right -= 1

        :param nums:
        :param two_sum:
        :return:
        """
        left = 0
        right = len(nums) - 1
        res = []
        while left < right:
            if nums[right] + nums[left] == two_sum:
                if [nums[left], nums[right]] not in res:
                    res.append([nums[left], nums[right]])
                left += 1
            elif nums[right] + nums[left] > two_sum:
                right -= 1
            else:
                left += 1
        return res
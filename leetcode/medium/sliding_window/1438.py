# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2021/2/21 9:54
"""

from typing import List
from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # ans = 0
        # N = len(nums)
        # for left in range(N):
        #     for right in range(left+1, N+1):
        #         sub_num = nums[left:right]
        #         if len(sub_num) == 1:
        #             ans = max(ans, 1)
        #         mininum, maximum = min(sub_num), max(sub_num)
        #         if maximum - mininum <= limit:
        #             ans = max(ans, right-left)
        #         else:
        #             break
        # return ans
        ans = 0
        sub_nums = SortedList()
        N = len(nums)
        left, right = 0, 0

        while right < N:
            sub_nums.add(nums[right])

            while sub_nums[-1] - sub_nums[0] > limit:
                sub_nums.remove(nums[left])
                left += 1 # 左指针被动右移（不满足条件时移动）

            ans = max(ans, right-left + 1)
            right += 1 # 右指针主动右移

        return ans



if __name__ == '__main__':
    s = Solution()
    nums = [8,2,4, 7]
    limit = 4
    print(s.longestSubarray(nums, limit))

    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    print(s.longestSubarray(nums, limit))

    nums = [4, 2, 2, 2, 4, 4, 2, 2]
    limit = 0
    print(s.longestSubarray(nums, limit))


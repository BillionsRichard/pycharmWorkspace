# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/12/22 23:14
"""
from typing import List
import heapq

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        if k == 1:
            return True
        #
        nums.sort()
        # while nums:
        #     min_num = nums[0]
        #     max_num = nums[0] + k - 1
        #     for i in range(max_num, min_num-1, -1):
        #         if i in nums:
        #             nums.remove(i)
        #         else:
        #             return False
        # return True
        heapq.heapify(nums)
        while nums:
            cur_min = heapq.heappop(nums)
            for i in range(1, k):
                try:
                    nums.remove(i + cur_min)
                except Exception as e:
                    print(e)
                    return False
        return True



if __name__ == '__main__':
    s = Solution()
    print(s.isPossibleDivide([1,2,3,3,4,4,5,6], 4))
    print(s.isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11], 3))
    print(s.isPossibleDivide([3,3,2,2,1,1], 3))
    print(s.isPossibleDivide([1,2,3,4], 3))
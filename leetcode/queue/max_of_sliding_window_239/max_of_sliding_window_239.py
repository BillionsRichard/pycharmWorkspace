# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/11/30 20:03
"""

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """使用双端队列，队列大小保持为 k。
        返回元素个数： len(nums) - k + 1

        :param nums:
        :param k:
        :return:
        """
        if not nums:
            return []

        win_queue = deque(nums[:k], maxlen=k)
        ans = [max(win_queue)]
        for num in nums[k:]:
            win_queue.popleft()
            win_queue.append(num)
            ans.append(max(win_queue))
        return ans







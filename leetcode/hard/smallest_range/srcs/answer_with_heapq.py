# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/13 20:34 
"""
from pprint import pprint as pp
from hard.smallest_range.srcs.big_2d_list import BIG_LIST_85
from hard.smallest_range.srcs.big_2d_list import BIG_LIST_86
import heapq


class Solution:
    def smallestRange(self, nums):
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        print('heap', heap)
        heapq.heapify(heap) # 最小值堆中存储的元素(元素， 行号，列）
        print('heapified:', heap)
        ans = -1e5, 1e5
        right = max(heap)[0]
        print('right:', right)

        while heap:
            left, i, j = heapq.heappop(heap) # 弹出最小值，行号，列号
            if right - left < ans[1] - ans[0]:
                ans = left, right

            if j + 1 == len(nums[i]):
                return ans

            v = nums[i][j + 1] # 弹出的那一行，向前移动1列
            right = max(right, v)
            heapq.heappush(heap, (v, i, j + 1))


if __name__ == '__main__':
    s = Solution()

    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    # nums = [[10], [11]]
    # nums = [[11,38,83,
    # 84,84,85,88,89,89,92],[28,61,89],[52,77,79,80,81],[21,25,26,26,26,27],[9,83,85,90],[84,85,87],[26,68,70,71],[36,40,41,42,45],[-34,21],[-28,-28,-23,1,13,21,28,37,37,38],[-74,1,2,22,33,35,43,45],[54,96,98,98,99],[43,54,60,65,71,75],[43,46],[50,50,58,67,69],[7,14,15],[78,80,89,89,90],[35,47,63,69,77,92,94]]
    #         [-74, 1, 2, 22, 33, 35, 43, 45], [54, 96, 98, 98, 99], [43, 54, 60, 65, 71, 75], [43, 46],
    #         [50, 50, 58, 67, 69], [7, 14, 15], [78, 80, 89, 89, 90], [35, 47, 63, 69, 77, 92, 94]]
    nums = BIG_LIST_85
    # nums = BIG_LIST_86
    min_range = s.smallestRange(nums)
    print(min_range)

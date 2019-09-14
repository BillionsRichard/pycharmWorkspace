# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/12 20:37 
"""
from pprint import pprint as pp
from operator import itemgetter
import time
from collections import OrderedDict
from hard.smallest_range.srcs.big_2d_list import BIG_LIST_85
from hard.smallest_range.srcs.big_2d_list import BIG_LIST_86


class Solution:
    """
    输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    输出: [20,24]
    """

    def smallestRange(self, nums):
        start_time = time.time()
        k = len(nums)
        print('k-->', k)
        k_tagged_merged_list = []
        for i in range(k):
            row = nums[i]
            k_tagged_merged_list.extend([(e, i) for e in row])

        k_tagged_merged_list.sort(key=itemgetter(0))
        sort_end_time = time.time()
        print('sorting time:', sort_end_time - start_time)

        # print(k_tagged_merged_list)
        od = OrderedDict()

        min_range = None
        min_range_len = int(2e5)
        # print('min_range_len', min_range_len)
        tot_len = len(k_tagged_merged_list)
        # print('tot_len', tot_len)
        i = 0
        while i < tot_len:
            this_tag = k_tagged_merged_list[i][1]
            cur_tag_set = od.keys()

            if this_tag in cur_tag_set:
                od.pop(this_tag)

            od[this_tag] = k_tagged_merged_list[i][0]

            tags = od.keys()
            # print('len_k_dque-->', len(k_dque))
            # print('len_k_dque_tags-->', len(k_dque_tags))

            if len(tags) == k:
                keys = list(od.keys())
                first_v = od[keys[0]]
                last_v = od[keys[-1]]

                k_range_len = last_v - first_v
                if k_range_len < min_range_len:
                    min_range_len = k_range_len
                    min_range = first_v, last_v
            i += 1

        print('ending main time:', time.time() - sort_end_time)
        return min_range


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

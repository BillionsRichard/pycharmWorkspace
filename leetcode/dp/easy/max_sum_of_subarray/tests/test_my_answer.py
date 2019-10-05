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
from pprint import pprint as pp
from dp.easy.max_sum_of_subarray.srcs.my_answer import Solution

import unittest


class TestMaxSumOfPartitionedArray(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        exp = 6
        act = Solution().maxSubArray(nums)
        self.assertEqual(exp, act)

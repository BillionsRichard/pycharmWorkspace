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
import unittest

from dp.easy.max_sum_of_subarray.srcs.offical_answer_with_divide_and_conquer import \
    Solution


class TestMaxSumOfSubArray(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        exp = 6
        act = Solution().maxSubArray(nums)
        self.assertEqual(exp, act)

    def test_2(self):
        nums = [1,2,-1]
        exp = 3
        act = Solution().maxSubArray(nums)
        self.assertEqual(exp, act)

    def test_3(self):
        nums = [2,-1,1,1]
        exp = 3
        act = Solution().maxSubArray(nums)
        self.assertEqual(exp, act)

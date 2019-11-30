# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/11/30 20:15
"""
from queue.max_of_sliding_window_239.max_of_sliding_window_239 import Solution
import unittest

class TestMaxOfSlidingWindow(unittest.TestCase):
    def setUp(self):pass
    def tearDown(self):pass
    def test_1(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        exp =  [3, 3, 5, 5, 6, 7]
        act = Solution().maxSlidingWindow(nums, k)
        self.assertEqual(exp, act)
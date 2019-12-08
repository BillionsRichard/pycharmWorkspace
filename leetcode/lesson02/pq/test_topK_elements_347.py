# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/12/1 12:32
"""
from lesson02.pq.topk_frequent_elements_347 import Solution
import unittest


class TestTopKElements(unittest.TestCase):
    def setUp(self): pass

    def tearDown(self): pass

    def test_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        exp = [1, 2]
        act = Solution().topKFrequent(nums, k)
        self.assertEqual(exp, act)

    def test_2(self):
        nums = [1]
        k = 1
        exp = [1]
        act = Solution().topKFrequent(nums, k)
        self.assertEqual(exp, act)

    def test_3(self):
        """
        :return:
        """
        nums = [5,2,5,3,5,3,1,1,3]
        k = 2
        exp = [3, 5]
        act = Solution().topKFrequent(nums, k)
        self.assertEqual(exp, act)

# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/4 15:09 
"""
import unittest
from dp.easy.range_sum_query.srcs.my_answer import NumArray


class TestFindItinerary(unittest.TestCase):
    def setUp(self):
        nums = [-2, 0, 3, -5, 2, -1]
        self.obj = NumArray(nums)

    def tearDown(self):
        pass

    def test_1(self):

        # sumRange(0, 2) -> 1
        # sumRange(2, 5) -> -1
        # sumRange(0, 5) -> -3

        exp = 1
        act = self.obj.sumRange(0, 2)
        self.assertEqual(exp, act)

    def test_2(self):

        # sumRange(0, 2) -> 1
        # sumRange(2, 5) -> -1
        # sumRange(0, 5) -> -3

        exp = -1
        act = self.obj.sumRange(2, 5)
        self.assertEqual(exp, act)

    def test_3(self):

        # sumRange(0, 2) -> 1
        # sumRange(2, 5) -> -1
        # sumRange(0, 5) -> -3

        exp = -3
        act = self.obj.sumRange(0, 5)
        self.assertEqual(exp, act)
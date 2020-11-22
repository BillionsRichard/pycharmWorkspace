# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/12/22 23:28
"""
import unittest
from week_race.virtual_race.divide_array_in_consecutive_nums import Solution
from week_race.virtual_race.big_input import BIG_LIST
from week_race.virtual_race.big_input import K


class TestIsCanDivide(unittest.TestCase):
    def setUp(self): pass

    def tearDown(self): pass

    def test_1(self):
        self.assertTrue(Solution().isPossibleDivide(BIG_LIST, K))

    def test_2(self):
        nums = [15,16,17,18,19,16,17,18,19,20,6,7,8,9,10,3,4,5,6,20]
        k = 5
        self.assertFalse(Solution().isPossibleDivide(nums, k))

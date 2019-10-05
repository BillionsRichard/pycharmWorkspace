# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/4 16:03 
"""
from dp.easy.climbing_staris_with_min_cost.srcs.my_answer import Solution
import unittest


class TestClimbingStairsWithMinCost(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_0(self):
        cost = [10, 15]
        exp = 10
        act = Solution().minCostClimbingStairs(cost)
        self.assertEqual(exp, act)

    def test_00(self):
        cost = [15, 10]
        exp = 10
        act = Solution().minCostClimbingStairs(cost)
        self.assertEqual(exp, act)

    def test_1(self):
        cost = [10, 15, 20]
        exp = 15
        act = Solution().minCostClimbingStairs(cost)
        self.assertEqual(exp, act)

    def test_2(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        exp = 6
        act = Solution().minCostClimbingStairs(cost)
        self.assertEqual(exp, act)

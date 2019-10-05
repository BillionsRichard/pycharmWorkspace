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
from dp.easy.house_robber.srcs.my_answer import Solution
import unittest


class TestClimbingStairsWithMinCost(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_0(self):
        cost = [1, 2, 3, 1]
        exp = 4
        act = Solution().rob(cost)
        self.assertEqual(exp, act)

    def test_1(self):
        cost = [2, 7, 9, 3, 1]
        exp = 12
        act = Solution().rob(cost)
        self.assertEqual(exp, act)

    def test_2(self):
        cost = [1]
        exp = 1
        act = Solution().rob(cost)
        self.assertEqual(exp, act)

    def test_3(self):
        cost = []
        exp = 0
        act = Solution().rob(cost)
        self.assertEqual(exp, act)

    def test_4(self):
        cost = [2, 1, 1, 2]
        exp = 4
        act = Solution().rob(cost)
        self.assertEqual(exp, act)

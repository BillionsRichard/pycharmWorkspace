# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/6 21:50 
"""
from graph.hard.swim_in_rising_pool.srcs.my_answer import Solution
import unittest


class TestSwimInRisingPool(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        grid = [[0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6]]
        exp = 16
        act = Solution().swimInWater(grid)
        self.assertEqual(exp, act)

    def test_2(self):
        grid = [[0, 2], [1, 3]]
        exp = 3
        act = Solution().swimInWater(grid)
        self.assertEqual(exp, act)

    def test_3(self):
        grid = [[0, 1, 4],
                [2, 8, 7],
                [3, 6, 5]]
        exp = 6
        act = Solution().swimInWater(grid)
        self.assertEqual(exp, act)

# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/11 22:01 
"""
import unittest
from graph.medium.number_of_islands_200.my_answer import Solution


class TestNumIslands(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        grid = ['11110', '11010', '11000', '00000']
        exp =1
        act = Solution().numIslands(grid)

        self.assertEqual(exp, act)

    def test_2(self):
        grid =['11000', '11000', '00100', '00011']
        exp =3
        act = Solution().numIslands(grid)

        self.assertEqual(exp, act)

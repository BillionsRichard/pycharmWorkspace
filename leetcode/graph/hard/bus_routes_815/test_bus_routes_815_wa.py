# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/27 15:51 
"""
from pprint import pprint as pp

from graph.hard.bus_routes_815.bus_routes_815_wa import Solution
import unittest


class TestBusRoutes(unittest.TestCase):
    def setUp(self): pass

    def tearDown(self): pass

    def test_1(self):
        routes = [[2], [2, 8]]
        S = 2
        T = 8
        exp = 1
        act = Solution().numBusesToDestination(routes, S, T)
        self.assertEqual(exp, act)

    def test_2(self):
        routes = [[0, 4, 15], [17, 20], [4, 11, 14, 16, 23], [1, 12, 15, 16],
                  [0, 6, 8, 10]]
        S = 10
        T = 0
        exp = 0
        act = Solution().numBusesToDestination(routes, S, T)
        self.assertEqual(exp, act)

    def test_3(self):
        routes = [[0, 1, 6, 16, 22, 23],
                  [14, 15, 24, 32],
                  [4, 10, 12, 20, 24, 28, 33],
                  [1, 10, 11, 19, 27, 33],
                  [11, 23, 25, 28],
                  [15, 20, 21, 23, 29],
                  [29]]
        S = 4
        T = 21
        exp = 2
        act = Solution().numBusesToDestination(routes, S, T)
        self.assertEqual(exp, act)

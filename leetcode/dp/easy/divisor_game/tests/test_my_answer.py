# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/4 10:43 
"""
import unittest
from dp.easy.divisor_game.srcs.my_answer import Solution


class TestDivisorGame(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        N = 2
        exp = True
        act = Solution().divisorGame(N)
        self.assertEqual(exp, act)

    def test_2(self):
        N = 3
        exp = False
        act = Solution().divisorGame(N)
        self.assertEqual(exp, act)
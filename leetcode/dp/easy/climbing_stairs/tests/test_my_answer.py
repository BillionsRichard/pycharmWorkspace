# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/4 15:41 
"""
from dp.easy.climbing_stairs.srcs.my_answer import Solution
import unittest

class TestClibmingStairs(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        n = 1
        exp = 1
        act = Solution().climbStairs(n)
        self.assertEqual(exp, act)

    def test_2(self):
        n = 2
        exp = 2
        act = Solution().climbStairs(n)
        self.assertEqual(exp, act)

    def test_3(self):
        n = 3
        exp = 3
        act = Solution().climbStairs(n)
        self.assertEqual(exp, act)
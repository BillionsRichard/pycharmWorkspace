# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 20:22 
"""
from pprint import pprint as pp
from graph.easy.find_the_town_judge.srcs.my_answer import Solution

import unittest

class TestFindJudgeOfTheTow(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        N = 2
        trust = [[1, 2]]
        exp = 2
        act = Solution().findJudge(N, trust)
        self.assertEqual(exp, act)

    def test_2(self):
        N = 3
        trust = [[1, 3], [2, 3]]
        exp = 3
        act = Solution().findJudge(N, trust)
        self.assertEqual(exp, act)

    def test_3(self):
        N = 3
        trust = [[1,3],[2,3],[3,1]]
        exp = -1
        act = Solution().findJudge(N, trust)
        self.assertEqual(exp, act)

    def test_4(self):
        N = 3
        trust = [[1, 2], [2, 3]]
        exp = -1
        act = Solution().findJudge(N, trust)
        self.assertEqual(exp, act)

    def test_5(self):
        N = 4
        trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
        exp = 3
        act = Solution().findJudge(N, trust)
        self.assertEqual(exp, act)
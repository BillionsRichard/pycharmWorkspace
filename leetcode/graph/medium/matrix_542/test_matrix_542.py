# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:
@software: PyCharm
@time: 2019/12/29 11:50
"""
from graph.medium.matrix_542.matrix_542 import Solution
import unittest


class TestMatrix542(unittest.TestCase):
    def setUp(self): pass

    def tearDown(self): pass

    def test_1(self):
        s = Solution()
        m = [[0, 0, 0],
             [0, 1, 0],
             [0, 0, 0]]
        exp = [[0, 0, 0],
               [0, 1, 0],
               [0, 0, 0]]
        act = s.updateMatrix(m)
        self.assertEqual(exp, act)

    def test_2(self):
        s = Solution()
        m = [[0, 0, 0],
             [0, 1, 0],
             [1, 1, 1]]
        exp = [[0, 0, 0],
               [0, 1, 0],
               [1, 2, 1]]
        act = s.updateMatrix(m)
        self.assertEqual(exp, act)

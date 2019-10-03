# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 21:43 
"""
import unittest
from graph.medium.regions_cut_by_slashes.srcs.my_answer import Solution


class TestFindItinerary(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        grid = [
            " /",
            "/ "
        ]
        exp = 2
        act = Solution().regionsBySlashes(grid)

        self.assertEqual(exp, act)

    def test_2(self):
        grid = [
            " /",
            "  "
        ]
        exp = 1
        act = Solution().regionsBySlashes(grid)

        self.assertEqual(exp, act)

    def test_3(self):
        grid = [
            "\\/",
            "/\\"
        ]
        exp = 4
        act = Solution().regionsBySlashes(grid)

        self.assertEqual(exp, act)

    def test_4(self):
        grid = [
            "/\\",
            "\\/"
        ]
        exp = 5
        act = Solution().regionsBySlashes(grid)

        self.assertEqual(exp, act)

    def test_5(self):
        grid = [
            "//",
            "/ "
        ]
        exp = 3
        act = Solution().regionsBySlashes(grid)

        self.assertEqual(exp, act)

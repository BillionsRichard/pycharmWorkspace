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
from graph.medium.surrounded_regions_130.my_bad_answer_with_dfs import Solution


class TestSurroundedRegions(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        board = [['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'X']]

        exp = [['X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X'],
               ['X', 'O', 'X', 'X']]
        Solution().solve(board)

        self.assertEqual(board, exp)

    def test_2(self):
        board = [['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'O'],
                ['X', 'O', 'X', 'X']]

        exp = [['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'O'],
                ['X', 'O', 'X', 'X']]
        Solution().solve(board)

        self.assertEqual(board, exp)

    def test_3(self):
        """9 * 9 的 矩阵，DFS 会超时。

        :return:
        """
        board = [['O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                 ['O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X'],
                 ['O', 'X', 'O', 'X', 'O', 'O', 'O', 'O', 'X'],
                 ['O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O'],
                 ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
                 ['X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X'],
                 ['O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O'],
                 ['O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O'],
                 ['O', 'O', 'O', 'O', 'O', 'X', 'X', 'O', 'O']]

        exp = [['O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X'],
               ['O', 'X', 'O', 'X', 'O', 'O', 'O', 'O', 'X'],
               ['O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O'],
               ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
               ['X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X'],
               ['O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O', 'X', 'X', 'O', 'O']]
        Solution().solve(board)

        from pprint import pprint as pp
        print('board')
        pp(board)

        self.assertEqual(board, exp)


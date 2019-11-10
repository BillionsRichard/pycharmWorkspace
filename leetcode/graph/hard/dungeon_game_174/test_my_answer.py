# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/20 16:28 
"""
import unittest

from graph.hard.dungeon_game_174.my_answer import Solution


class TestMinHealthValue(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        """
        -2 (K)	-3	3
        -5	    -10	1
        10	    30	-5 (P)

        :return:
        """
        dungeon = [[-2, -3, 3],
                   [-5, -10, 1],
                   [10, 30, -5],
                   ]
        exp = 7
        act = Solution().calculateMinimumHP(dungeon)
        self.assertEqual(exp, act)

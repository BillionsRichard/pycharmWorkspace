# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2019/12/29 12:38
"""

import unittest
from recursion.kth_symbol_in_grammer_779.kth_symbol_in_grammar_779 import \
    Solution


class TestKthSymbolInGrammar779(unittest.TestCase):
    def setUp(self): pass

    def tearDown(self): pass

    def test_1(self):
        """
        0

        :return:
        """
        N = 1
        K = 1
        exp = 0
        act = Solution().kthGrammar(N, K)
        self.assertEqual(exp, act)

    def test_2(self):
        """
        0
        0 1
        :return:
        """
        N = 2
        K = 1
        exp = 0
        act = Solution().kthGrammar(N, K)
        self.assertEqual(exp, act)

    def test_3(self):
        """
        0
        0 1
        :return:
        """
        N = 2
        K = 2
        exp = 1
        act = Solution().kthGrammar(N, K)
        self.assertEqual(exp, act)

    def test_4(self):
        """
        0
        0 1
        0 1 1 0
        :return:
        """
        N = 3
        K = 1
        exp = 0
        act = Solution().kthGrammar(N, K)
        self.assertEqual(exp, act)

    def test_5(self):
        """
        0
        0 1
        0 1 1 0
        :return:
        """
        N = 3
        K = 2
        exp = 1
        act = Solution().kthGrammar(N, K)
        self.assertEqual(exp, act)

    def test_6(self):
        """
        0
        0 1
        0 1 1 0
        :return:
        """
        N = 3
        K = 3
        exp = 1
        act = Solution().kthGrammar(N, K)
        self.assertEqual(exp, act)

    def test_7(self):
        """
        0
        0 1
        0 1 1 0
        :return:
        """
        N = 3
        K = 4
        exp = 0
        act = Solution().kthGrammar(N, K)
        self.assertEqual(exp, act)

    def test_15(self):
        """
        0
        0 1
        0 1 1 0
        :return:
        """
        N = 30
        K = 434991989
        exp = 0
        act = Solution().kthGrammar(N, K)
        self.assertEqual(exp, act)

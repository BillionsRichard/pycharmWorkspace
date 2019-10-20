# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/19 8:13 
"""
import unittest

from string_handle.medium.word_break_139.word_break_OA_with_dp import Solution


class TestWordBreak(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_1(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        act = Solution().wordBreak(s, wordDict)
        self.assertEqual(act, True)

    def test_2(self):
        s = "applepenapple"
        wordDict =  ["apple", "pen"]
        act = Solution().wordBreak(s, wordDict)
        self.assertEqual(act, True)

    def test_3(self):
        s = "cars"
        wordDict =  ["car","ca","rs"]
        act = Solution().wordBreak(s, wordDict)
        self.assertEqual(act, True)

    def test_4(self):
        s = "catsandog"
        wordDict =  ["cats", "dog", "sand", "and", "cat"]
        act = Solution().wordBreak(s, wordDict)
        self.assertEqual(act, False)

    def test_5(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        act = Solution().wordBreak(s, wordDict)
        self.assertEqual(act, False)

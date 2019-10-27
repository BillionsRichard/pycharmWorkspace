# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/27 14:59 
"""
from pprint import pprint as pp
from string_handle.medium.phone_num_comb_17.phone_num_comb import Solution
import unittest

class TestPhoneNumCom(unittest.TestCase):
    def setUp(self):pass
    def tearDown(self):pass
    def test_1(self):
        digits = '23'
        exp = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        act = Solution().letterCombinations(digits)
        self.assertEqual(exp, act)
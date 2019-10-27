# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/27 11:38 
"""
from pprint import pprint as pp
from string_handle.medium.restore_ip_93.restore_ip import Solution
import unittest

class TestRestoreIP(unittest.TestCase):
    def setUp(self):pass
    def tearDown(self):pass
    def test_1(self):
        s = "25525511135"
        exp = ["255.255.11.135", "255.255.111.35"]
        act = Solution().restoreIpAddresses(s)
        self.assertEqual(exp, act)

    def test_2(self):
        s = "128128128123"
        exp = ["128.128.128.123"]
        act = Solution().restoreIpAddresses(s)
        self.assertEqual(exp, act)


    def test_3(self):
        s = "1111"
        exp = ["1.1.1.1"]
        act = Solution().restoreIpAddresses(s)
        self.assertEqual(exp, act)


    def test_4(self):
        s = "2552552551"
        exp = ["255.255.25.51",
               '255.255.255.1']
        act = Solution().restoreIpAddresses(s)
        self.assertEqual(exp, act)
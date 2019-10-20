# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/19 22:40 
"""
from pprint import pprint as pp
import unittest
from string_handle.medium.compare_versions.compare_version import Solution


class TestVersionCompare(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        version1 = "0.1"
        version2 = "1.1"
        exp = -1

        act = Solution().compareVersion(version1, version2)
        self.assertEqual(exp, act)

    def test_2(self):
        version1 = "1.0.1"
        version2 = "1"
        exp = 1

        act = Solution().compareVersion(version1, version2)
        self.assertEqual(exp, act)

    def test_3(self):
        version1 = "7.5.2.4"
        version2 = "7.5.3"
        exp = -1

        act = Solution().compareVersion(version1, version2)
        self.assertEqual(exp, act)

    def test_4(self):
        version1 = "1.01"
        version2 = "1.001"
        exp = 0

        act = Solution().compareVersion(version1, version2)
        self.assertEqual(exp, act)

    def test_5(self):
        version1 = "1.0"
        version2 = "1.0.0"
        exp = 0

        act = Solution().compareVersion(version1, version2)
        self.assertEqual(exp, act)

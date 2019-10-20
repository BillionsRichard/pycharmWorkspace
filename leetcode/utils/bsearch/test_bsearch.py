# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/20 10:01 
"""
from utils.bsearch.bisearch import bsearch
import unittest


class TestMyBsearch(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        l = []
        target = 0
        exp = -1
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_2(self):
        l = [0]
        target = 0
        exp = 0
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_3(self):
        l = [0, 1]
        target = 0
        exp = 0
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_4(self):
        l = [0, 1]
        target = 1
        exp = 1
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_5(self):
        l = [0, 1, 2]
        target = 1
        exp = 1
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_6(self):
        l = [0, 1, 2]
        target = 0
        exp = 0
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_7(self):
        l = [0, 1, 2]
        target = 2
        exp = 2
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_8(self):
        l = [0, 1, 2, 3]
        target = 0
        exp = 0
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_9(self):
        l = [0, 1, 2, 3]
        target = 1
        exp = 1
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_10(self):
        l = [0, 1, 2, 3]
        target = 2
        exp = 2
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_11(self):
        l = [0, 1, 2, 3]
        target = 3
        exp = 3
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_12(self):
        l = [0, 1, 2, 3]
        target = 4
        exp = -1
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_13(self):
        l = [0, 1, 2, 3]
        target = -1
        exp = -1
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_14(self):
        l = [0, 1, 2]
        target = -1
        exp = -1
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_15(self):
        l = [0, 1, 2]
        target = 3
        exp = -1
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_16(self):
        l = [0, 1, 2, 2, 3]
        target = 2
        exp = 2
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_17(self):
        l = [0, 1, 1, 2, 2, 3]
        target = 2
        exp = 4
        act = bsearch(target, l)
        self.assertEqual(exp, act)

    def test_18(self):
        l = [0, 1, 1, 2, 2, 3]
        target = 1
        exp =2
        act = bsearch(target, l)
        self.assertEqual(exp, act)

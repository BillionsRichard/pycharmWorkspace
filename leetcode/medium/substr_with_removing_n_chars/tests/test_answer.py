# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/8 9:38 
"""
from pprint import pprint as pp
import unittest
from srcs.medium.substr_with_removing_n_chars.srcs.answer import remove_n_chars_to_be_sub_str

class TestRemoveNCharsToBeSubStr(unittest.TestCase):
    def setUp(self):
        print('Setting up...')
    def tearDown(self):
        print('Tearing down...')

    def test_1(self):
        s = 'axb'
        p = 'ab'
        exptected_n = 1
        acutal = remove_n_chars_to_be_sub_str(s, p)
        self.assertEqual(exptected_n, acutal)

    def test_2(self):
        s = 'ab'
        p = 'ab'
        exptected_n = 0
        acutal = remove_n_chars_to_be_sub_str(s, p)
        self.assertEqual(exptected_n, acutal)

    def test_3(self):
        s = 'acbacdefacbab'
        p = 'ab'
        exptected_n = 0
        acutal = remove_n_chars_to_be_sub_str(s, p)
        self.assertEqual(exptected_n, acutal)

    def test_4(self):
        s = 'facbacdefacbabdfcadef'
        p = 'fdef'
        exptected_n = 2
        acutal = remove_n_chars_to_be_sub_str(s, p)
        self.assertEqual(exptected_n, acutal)

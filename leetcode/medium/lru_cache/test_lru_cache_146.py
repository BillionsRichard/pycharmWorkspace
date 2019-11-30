# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/11/17 11:02
"""
from medium.lru_cache.lru_cache_146 import LRUCache
import unittest

class TestLruCache(unittest.TestCase):
    def setUp(self):pass
    def tearDown(self):pass
    def test_5(self):
        c = LRUCache(1)
        c.put(2,1)
        self.assertEqual(1, c.get(2))
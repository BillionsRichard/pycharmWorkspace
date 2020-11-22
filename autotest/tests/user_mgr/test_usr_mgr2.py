# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/11/1 10:00
"""
import pytest

def setup_module():
    print("初始化模块")


def teardown_module():
    print("清除模块")


class TestWrongPassword:
    @classmethod
    def setup_class(cls):
        print("set up for class")

    @classmethod
    def teardown_class(cls):
        print("Teardown for class ")

    def test_0001(self):
        print("Test case 0001")
        assert 1 == 1

    def test_0002(self):
        print("Test case 0002")
        assert 2 == 2

    @pytest.mark.smoke
    def test_0003(self):
        print("Test case 0003")
        assert 3 == 3

    def test_密码错误(self):
        print("Test case 0004")
        assert 3 == 5

    def setup_method(self):
        print("方法初始化")

    def teardown_method(self):
        print("方法清除")

# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2021/1/10 10:43
"""

import pytest

from easy.summary_ranges.summary_range import Solution


@pytest.fixture(scope='session')
def get_solution():
    print('init---------->')
    return Solution()


class TestSummary:

    # @staticmethod
    def test_a(self, get_solution):
        nums = [0, 1, 2, 4, 5, 7]
        exp = ["0->2", "4->5", "7"]
        assert exp == get_solution.summaryRanges(nums)

    # @staticmethod
    def test_b(self, get_solution):
        nums = []
        exp = []
        assert exp == get_solution.summaryRanges(nums)

    # @staticmethod
    def test_c(self, get_solution):
        nums = [-1]
        exp = ["-1"]
        assert exp == get_solution.summaryRanges(nums)

    # @staticmethod
    def test_d(self, get_solution):
        nums = [0]
        exp = ["0"]
        assert exp == get_solution.summaryRanges(nums)


if __name__ == '__main__':
        pytest.main(["-s", "test_summary_range.py"]) # 调用pytest的main函数执行测试
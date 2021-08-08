# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2021/3/7 11:29
"""
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.isPalindrom = lambda s:s == s[::-1]
        res = []
        path = []
        self.backtrace(s, res, path)
        return res

    def backtrace(self, s, res, path):
        if not s:
            res.append(path)
            return

        for i in range(1, len(s)+1):
            if self.isPalindrom(s[:i]):
                self.backtrace(s[i:], res, path + [s[:i]])


if __name__ == '__main__':
    s = Solution()
    ss = 'aab'
    res = s.partition(ss)
    print(res)
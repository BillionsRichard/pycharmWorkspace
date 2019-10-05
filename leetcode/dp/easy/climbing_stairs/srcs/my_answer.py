# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/4 15:41 
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        res_dict = {1: 1, 2: 2}

        if n < 2:
            return res_dict.get(n)

        for i in range(3, n + 1):
            res_dict[i] = res_dict.get(i - 1) + res_dict.get(i - 2)
        return res_dict[n]

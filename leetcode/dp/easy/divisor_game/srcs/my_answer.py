# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/4 10:43 
"""


class Solution:
    def divisorGame(self, N: int) -> bool:
        find_cnt = 0
        while True:
            for x in range(1, N):
                if N % x == 0:
                    N = N - x
                    find_cnt += 1
                    break
            else:
                break

        return find_cnt % 2 == 1

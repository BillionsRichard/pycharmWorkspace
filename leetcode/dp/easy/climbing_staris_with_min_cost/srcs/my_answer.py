# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/4 16:03 
"""


class Solution:
    def minCostClimbingStairs(self, cost: list) -> int:
        list_len = len(cost)
        # if list_len == 2:
        #     return min(cost)

        res = [cost[0], cost[1]]
        for i in range(2, list_len):
            res_i = min(res[i-1] + cost[i],
                         res[i-2] + cost[i])
            res.append(res_i)

        return min(res[-1], res[-2])



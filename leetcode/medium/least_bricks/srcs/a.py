# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/14 22:47 
"""
from pprint import pprint as pp


class Solution:
    def leastBricks(self, wall):
        row_cnt = len(wall)
        row_brick_width_dict = dict()

        for row in wall:
            row_brick_num = len(row)
            brick_width_sum = 0
            for i in range(0, row_brick_num-1):
                brick_width_sum += row[i]
                old_cnt = row_brick_width_dict.setdefault(brick_width_sum, 0)
                row_brick_width_dict[brick_width_sum] = old_cnt + 1

        # pp(row_brick_width_dict)
        if not row_brick_width_dict:
            return row_cnt

        width_of_max_cnt = max(row_brick_width_dict, key=lambda k: row_brick_width_dict.get(k))
        max_cnt = row_brick_width_dict.get(width_of_max_cnt)
        # print('row_cnt:', row_cnt)
        # print('width_of_max_cnt:', width_of_max_cnt)
        # print('max_cnt:', max_cnt)

        return row_cnt - max_cnt

if __name__ == '__main__':
    s = Solution()
    wall = [[1,2,2,1],
      [3,1,2],
      [1,3,2],
      [2,4],
      [3,1,2],
      [1,3,1,1]]
    wall = [[1],[1],[1]]

    print(s.leastBricks(wall))












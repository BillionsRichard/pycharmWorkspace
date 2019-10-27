# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/20 16:28 
"""
class Solution:
    def calculateMinimumHP(self, dungeon: list) -> int:
        m,n = len(dungeon), len(dungeon[0])
        d = dungeon

        h = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if d[i][j] >= 0:
                    h[i][j] = 1
                else:
                    h[i][j] = 1 - d[i][j]


        queue = [(m-1, n-1)]
        while queue:
            cur_x,cur_y = queue.pop()
            cur_h = h[cur_x][cur_y]

            # 计算上一格最低的 h 值
            up_x,up_y = cur_x-1, cur_y

            h_up_right_cons, h_down_cons = 1, 1
            if up_y < n-1:# has right
                h_up_right = h[up_x][up_y+1]
                h_up_right_cons = max(h_up_right - d[up_x][up_y], 1)

            if up_x < m-1:# has down
                h_down = h[up_x+1][up_y]
                h_down_cons = max(1, h_down - d[up_x][up_y])

            # 计算左一格最低的 h 值

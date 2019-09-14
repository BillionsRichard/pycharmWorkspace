# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/14 9:24 
"""
from pprint import pprint as pp
from medium.map_analysis.srcs.big_matrix import BIG_GRID
from medium.map_analysis.srcs.big_matrix import BIG_GRID_13


class Solution:
    """牛逼的递归算法"""
    
    def maxDistance(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        a = [[2e4] * (cols + 2) for _ in range(rows + 2)]
        b = [[2e4] * (cols + 2) for _ in range(rows + 2)]
        c = [[2e4] * (cols + 2) for _ in range(rows + 2)]
        d = [[2e4] * (cols + 2) for _ in range(rows + 2)]
        s = 0
        for l in grid:
            s += sum(l)
        if s == 0 or s == rows * cols:
            return -1
        ans_list = []

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if grid[i - 1][j - 1] == 1:
                    a[i][j] = 0
                else:
                    a[i][j] = min(a[i - 1][j], a[i][j - 1]) + 1
        for i in range(1, rows + 1):
            for j in range(cols, 0, -1):
                if grid[i - 1][j - 1] == 1:
                    b[i][j] = 0
                else:
                    b[i][j] = min(b[i - 1][j], b[i][j + 1]) + 1
        for i in range(rows, 0, -1):
            for j in range(1, cols + 1):
                if grid[i - 1][j - 1] == 1:
                    c[i][j] = 0
                else:
                    c[i][j] = min(c[i + 1][j], c[i][j - 1]) + 1
        for i in range(rows, 0, -1):
            for j in range(cols, 0, -1):
                if grid[i - 1][j - 1] == 1:
                    d[i][j] = 0
                else:
                    d[i][j] = min(d[i + 1][j], d[i][j + 1]) + 1

        for i in range(rows, 0, -1):
            for j in range(1, cols + 1):
                if grid[i - 1][j - 1] == 0:
                    ans_list.append(min(a[i][j], b[i][j], c[i][j], d[i][j]))
        return max(ans_list)


if __name__ == '__main__':
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    grid = BIG_GRID
    grid = BIG_GRID_13
    s = Solution()

    import time
    start_time = time.time()
    md = s.maxDistance(grid)
    end_time = time.time()
    print('time:', end_time - start_time)
    print(md)

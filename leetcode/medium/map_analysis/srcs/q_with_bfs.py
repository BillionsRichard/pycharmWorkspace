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


class Solution:
    """"""
    def maxDistance(self, grid):
        land_cells = []
        ocean_cells = []
        m_len = len(grid)
        for i in range(m_len):
            for j in range(m_len):
                if grid[i][j] == 1:
                    land_cells.append((i, j))
                else:
                    ocean_cells.append((i, j))

        if not land_cells or not ocean_cells:
            return -1

        max_dis = None
        for ocean_cell in ocean_cells:
            min_dis = None
            for land_cell in land_cells:
                dis = Solution.get_manhattan_dis(ocean_cell, land_cell)
                if min_dis is None or min_dis>dis:
                    min_dis = dis
            if max_dis is None or max_dis < min_dis:
                max_dis = min_dis

        return max_dis

    @staticmethod
    def get_manhattan_dis(cell1, cell2):
        return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

    @staticmethod
    def go_one_step(land_cell, grid, min_dis):
        r, c = land_cell
        m_len = len(grid)
        # <--
        if c >= 1 and grid[r][c - 1] == 0:
            min_dis[r][c - 1] = 1
        # -->
        if c + 1 < m_len and grid[r][c + 1] == 0:
            min_dis[r][c + 1] = 1

        # /\
        # |
        if r >= 1 and grid[r - 1][c] == 0:
            min_dis[r - 1][c] = 1

        #  |
        # \/
        if r >= 1 and grid[r - 1][c] == 0:
            min_dis[r - 1][c] = 1


if __name__ == '__main__':
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    grid = BIG_GRID
    s = Solution()

    import time
    start_time = time.time()
    md = s.maxDistance(grid)
    end_time = time.time()
    print('time:', end_time - start_time)
    print(md)

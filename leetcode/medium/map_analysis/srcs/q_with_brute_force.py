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
    """Timed out"""

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

        max_dis = -1
        for ocean_cell in ocean_cells:
            min_dis = 9999
            for land_cell in land_cells:
                dis = Solution.get_manhattan_dis(ocean_cell, land_cell)
                if min_dis > dis:
                    min_dis = dis

                if min_dis == 1:
                    break

            if max_dis < min_dis:
                max_dis = min_dis

        return max_dis

    @staticmethod
    def get_manhattan_dis(cell1, cell2):
        return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])


if __name__ == '__main__':
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    grid = BIG_GRID
    # grid = BIG_GRID_13
    s = Solution()

    import time
    start_time = time.time()
    md = s.maxDistance(grid)
    end_time = time.time()
    print('time:', end_time - start_time)
    print(md)

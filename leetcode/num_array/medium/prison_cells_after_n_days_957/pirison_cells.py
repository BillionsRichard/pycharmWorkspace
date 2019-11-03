# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/11/3 9:22 
"""
from pprint import pprint as pp


class Solution(object):

    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        # N >= 1
        if N == 0:
            return cells

        CACHE = dict()
        cell_num = len(cells)
        XNOR = [1, 0]

        new_cells = cells[:]
        for j in range(0, cell_num):
            # 第一个和最后一个特殊处理。
            if j == 0 or j == cell_num - 1:
                if cells[j] == 1:
                    new_cells[j] = 0
                continue

            new_cells[j] = XNOR[cells[j - 1] ^ cells[j + 1]]

        cells = new_cells
        CACHE[1] = cells[:]

        for i in range(2, 15):
            new_cells = cells[:]
            for j in range(1, cell_num - 1):
                new_cells[j] = XNOR[cells[j - 1] ^ cells[j + 1]]

            CACHE[i % 14] = new_cells[:]
            cells = new_cells[:]

        return CACHE[N % 14]


if __name__ == '__main__':
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    N = 7
    exp = [0, 0, 1, 1, 0, 0, 0, 0]

    s = Solution()
    r = s.prisonAfterNDays(cells, N)
    print(r)

    N = 14
    print(s.prisonAfterNDays(cells, N))

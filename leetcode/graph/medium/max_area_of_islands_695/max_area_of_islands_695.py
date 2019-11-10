# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/11/10 17:11 
"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ones = []
        visited = [[False for _ in range(n)]
                   for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones.append((i, j))

        if not ones:
            return 0

        xdir = [-1, 1, 0, 0]
        ydir = [0, 0, -1, 1]
        max_area = 0

        for x, y in ones:
            if visited[x][y]:
                continue

            visited[x][y] = True
            queue = [(x, y)]
            cur_max = 1
            while queue:
                x, y = queue.pop(0)

                for i in range(4):
                    new_x = x + xdir[i]
                    new_y = y + ydir[i]
                    if (new_x in range(m)
                            and new_y in range(n)
                            and grid[new_x][new_y] == 1
                            and not visited[new_x][new_y]):
                        visited[new_x][new_y] = True
                        cur_max += 1
                        queue.append((new_x, new_y))

            max_area = max(cur_max, max_area)
        return max_area

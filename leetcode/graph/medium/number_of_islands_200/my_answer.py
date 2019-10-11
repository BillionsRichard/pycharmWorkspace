# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/11 22:01 
"""
"""
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，
并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水
包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def numIslands(self, grid: list) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        xdir = [0, 0, -1, 1]
        ydir = [1, -1, 0, 0]

        visit = dict()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    visit[(i, j)] = False

        if len(visit) == 0:
            return 0
        if len(visit) == n * m:
            return 1

        def bfs(startx, starty):
            queue = [(startx, starty)]
            visit[(startx, starty)] = True
            while queue:
                x, y = queue.pop(0)
                new_pos = [(x + xdir[i], y + ydir[i]) for i in range(4)]
                for new_x, new_y in new_pos:
                    if new_x in range(m) and new_y in range(n) \
                            and grid[new_x][new_y] == '1' \
                            and not visit[(new_x, new_y)]:
                        queue.append((new_x, new_y))
                        visit[(new_x, new_y)] = True

        ans = 0
        while True:
            not_visited_land_cell = list(filter(lambda pos: not visit[pos],
                                                visit.keys()))

            if not_visited_land_cell:
                ans += 1
                startx, starty = not_visited_land_cell[0]
                # print('starx,stary', (startx,starty))
                bfs(startx, starty)
            else:
                break

        return ans

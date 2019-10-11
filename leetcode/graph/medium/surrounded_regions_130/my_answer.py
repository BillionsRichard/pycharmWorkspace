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
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何
不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平
或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
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

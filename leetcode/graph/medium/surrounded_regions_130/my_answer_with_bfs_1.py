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
    def solve(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        解题思路：正向思维：将所有的边界 O 联通区域通过 BFS 算法遍历并记录下来。
        最后遍历整个地图，不在这些边界 O 联通区域的 O 改写成'X'。

        能直接找到环绕 O 联通区域么？不好找。

        """
        if not board:
            return

        m, n = len(board), len(board[0])

        # 记录 O 的访问状态
        v = dict()
        # BFS 队列。
        q = []
        all_o_cnt = 0

        # 所有可达边界 O 的点的集合。
        all_reaching_edege_os = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    v[(i, j)] = False
                    all_o_cnt += 1
                    if i in [0, m - 1] or j in [0, n - 1]:
                        q.append((i, j))
                        v[(i, j)] = True
                        all_reaching_edege_os.append((i,j))

        # 无边界 O 则 翻转全部 O
        if not q:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
            return

        # 全部是 O, 直接返回。
        if all_o_cnt == m * n:
            return

        def bfs():
            # 定义 BFS 方向： 上下左右 顺序搜索。
            xdir = [-1, 1, 0, 0]
            ydir = [0, 0, -1, 1]

            while q:
                x, y = q.pop(0)
                next_pos = [(x + xdir[k], y + ydir[k]) for k in range(4)]
                for next_x, next_y in next_pos:
                    if (next_x in range(m) and next_y in range(n)
                            and board[next_x][next_y] == 'O'
                            and not v[(next_x, next_y)]):
                        q.append((next_x, next_y))
                        v[(next_x, next_y)] = True
                        all_reaching_edege_os.append((next_x, next_y))

        bfs()

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in all_reaching_edege_os:
                    board[i][j] = 'X'

        return



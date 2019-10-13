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
        """
        if not board:
            return

        m, n = len(board), len(board[0])

        # 记录所有的 边界 O 点。
        o_cnt = 0
        queue = []
        for i in range(0, m):
            for j in range(0, n):
                if (i in [0, m - 1] or j in [0, n - 1]) and board[i][j] == 'O':
                    queue.append((i, j))

                if board[i][j] == 'O':
                    o_cnt += 1

        # 全 O
        if o_cnt == m * n:
            return

        # 没有边界 O
        if not queue:
            for i in range(0, m):
                for j in range(0, n):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
            return

        # 搜索方向顺序：右-> 左 -> 下 -> 上
        xdir = [0, 0, 1, -1]
        ydir = [1, -1, 0, 0]

        # 所有边界 O 入队。

        def bfs():
            """ 广度优先搜索算法。
            采用逆向思维： 首先所有的边界 O 点入队；然后依次出队遍历，

            1、出队后 O 改为 'Y'，充当了 边界 O 联通的区域 O 的访问标记。
            2、同时向 上下左右 四个方向看是否有 O。如有，则入队。

            编写要点：飞递归算法；运用队列结构。

            :return:
            """

            while queue:
                cur_x, cur_y = queue.pop(0)
                board[cur_x][cur_y] = 'Y'

                new_poses = [(cur_x + xdir[k], cur_y + ydir[k])
                             for k in range(4)]

                for new_x, new_y in new_poses:
                    if (new_x in range(m) and new_y in range(n)
                            and board[new_x][new_y] == 'O'):
                        queue.append((new_x, new_y))

        bfs()

        # print('board after BFSed')
        # from pprint import pprint as pp
        # pp(board)

        # 所有边界 O 联通的区域 O 被改写成了 Y, 需要 恢复成 O
        # 其他被环绕的 O 未被 BFS 遍历到，需要翻转成 X。
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                    continue  # important

                if board[i][j] == 'O':
                    board[i][j] = 'X'

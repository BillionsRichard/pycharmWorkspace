# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/13 17:28 
"""
from pprint import pprint as pp


class Solution:
    # def solveNQueens(self, n: int) -> List[List[str]]:
    def solveNQueens(self, n: int) -> list:
        """解题思路：隐式图搜索， 用 DFS 算法

         假设 N = 4
        搜索起始点：第一个皇后位置
                有四个位置可选：依次位于第 0，1，2，3列中。

        :param n:
        :return:
        """
        if n <= 3:
            return

        queen_col_visit = {i: False for i in range(n)}
        # queen_col_visit = [False for i in range(n)]
        queen_row_visit = {i: False for i in range(n)}
        # queen_row_visit = {i: False for i in range(n)}
        main_diag = {i: False for i in range(2 * n - 1)}
        minor_diag = {i: False for i in range(1 - n, n)}
        queen_col_index_list = []
        queen_poses = []
        xdir = [-1, -2, -2, -1, +1, +2, +2, +1]
        ydir = [-2, -1, +1, +2, +2, +1, -1, -2]

        def dfs(cur_x, cur_y):
            # queen_cols = list(filter(lambda col: queen_col_visit[col],
            #                          queen_col_visit))
            if len(queen_poses) == n:
                queen_col_index_list.append(queen_poses[:])
                queen_poses.clear()
                return

            # new_pos = [(cur_x + xdir[k], cur_y + ydir[k]) for k in range(8)]
            # for next_x, next_y in new_pos:
            for next_x in range(n):
                for next_y in range(n):
                    if (next_x in range(n)
                            and next_y in range(n)
                            and not queen_row_visit[next_x]
                            and not queen_col_visit[next_y]
                            and not main_diag[next_x + next_y]
                            and not minor_diag[next_x - next_y]):
                        queen_row_visit[next_x] = True
                        queen_col_visit[next_y] = True
                        main_diag[next_x + next_y] = True
                        minor_diag[next_x - next_y] = True

                        queen_poses.append((next_x, next_y))
                        dfs(next_x, next_y)

                        queen_row_visit[next_x] = False
                        queen_col_visit[next_y] = False
                        main_diag[next_x + next_y] = False
                        minor_diag[next_x - next_y] = False

        for i in range(n):
            queen_row_visit[0] = True
            queen_col_visit[i] = True
            main_diag[i] = True
            minor_diag[0 - i] = True

            queen_poses.append((0,i))
            dfs(0, i)

            queen_row_visit[0] = False
            queen_col_visit[i] = False
            main_diag[i] = False
            minor_diag[0 - i] = False


        return queen_col_index_list


if __name__ == '__main__':
    N = 4
    from pprint import pprint as pp

    r = Solution().solveNQueens(N)
    pp(r)

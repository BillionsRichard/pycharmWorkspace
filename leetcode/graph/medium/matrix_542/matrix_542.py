# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/12/29 11:37
"""

"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
在真实的面试中遇到过这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/01-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

from typing import List
from collections import deque
from collections import defaultdict


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def bfs(x, y):
            if matrix[x][y] == 0:
                return 0
            visited = defaultdict(bool)
            q = deque([(x, y, 0)])
            visited[(x, y)] = True

            while q:
                cx, cy, step = q.popleft()
                if matrix[cx][cy] == 0:
                    return step

                for d in range(4):
                    nx = cx + dx[d]
                    ny = cy + dy[d]
                    if nx in range(m) and ny in range(n) and not visited[(
                            nx, ny)]:
                        if matrix[nx][ny] == 0:
                            return step + 1

                        q.append((nx, ny, step + 1))
                        visited[(nx, ny)] = True

        return [[bfs(i, j) for j in range(n)] for i in range(m)]

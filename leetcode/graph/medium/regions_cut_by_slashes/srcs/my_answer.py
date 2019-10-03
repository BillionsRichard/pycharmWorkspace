# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/3 12:36 
"""
"""
在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些
字符会将方块划分为一些共边的区域。

（请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。

返回区域的数目。

 

示例 1：

输入：
[
  " /",
  "/ "
]
输出：2
解释：2x2 网格如下：

示例 2：

输入：
[
  " /",
  "  "
]
输出：1
解释：2x2 网格如下：

示例 3：

输入：
[
  "\\/",
  "/\\"
]
输出：4
解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
2x2 网格如下：

示例 4：

输入：
[
  "/\\",
  "\\/"
]
输出：5
解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
2x2 网格如下：

示例 5：

输入：
[
  "//",
  "/ "
]
输出：3
解释：2x2 网格如下：

 

提示：

1 <= grid.length == grid[0].length <= 30
grid[i][j] 是 '/'、'\'、或 ' '。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regions-cut-by-slashes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from pprint import pprint as pp


class Solution:
    def regionsBySlashes(self, grid: list) -> int:
        new_grid = Solution.three_times_grid(grid)
        pp(new_grid)

        res = 0
        new_len = len(new_grid)
        for i in range(new_len):
            for j in range(new_len):
                if not new_grid[i][j]:
                    Solution.dfs(new_grid, i, j)
                    res += 1
        return res

    @staticmethod
    def dfs(grid, i, j):
        """深度优先搜索递归算法：
        当前方格（i,j） 位置如果为 0，将当前坐标标记为 1，
        然后分别向 上、下、左、右 四个方向 递归 搜索。

        :param grid: 方格数组
        :param i: 当前方格横坐标
        :param j: 当前方格纵坐标
        :return:
        """
        grid_len = len(grid)
        if 0 <= i < grid_len and 0 <= j < grid_len and not grid[i][j]:
            grid[i][j] = 1
            Solution.dfs(grid, i - 1, j)
            Solution.dfs(grid, i + 1, j)
            Solution.dfs(grid, i, j - 1)
            Solution.dfs(grid, i, j + 1)

    @staticmethod
    def three_times_grid(grid: list):
        """将每个方格转换成三行三列的0和1构成的新方格；用1表示存在斜线
        如 输入为 : [ ' \',
                     '/ ']
            转化成：
                   [0 0 0 1 0 0
                    0 0 0 0 1 0
                    0 0 0 0 0 1
                    0 0 1 0 0 0
                    0 1 0 0 0 0
                    1 0 0 0 0 0]
        最终问题转换成求 0 的联通区域 个数。
        """
        grid_len = len(grid)
        new_len = 3 * grid_len
        new_grid = [[0 for col in range(new_len)] for row in
                    range(new_len)]

        for i in range(grid_len):
            for j in range(grid_len):
                if grid[i][j] == '/':
                    new_grid[3 * i][3 * j + 2] = 1
                    new_grid[3 * i + 1][3 * j + 1] = 1
                    new_grid[3 * i + 2][3 * j + 0] = 1
                if grid[i][j] == '\\':
                    new_grid[3 * i][3 * j] = 1
                    new_grid[3 * i + 1][3 * j + 1] = 1
                    new_grid[3 * i + 2][3 * j + 2] = 1
        return new_grid

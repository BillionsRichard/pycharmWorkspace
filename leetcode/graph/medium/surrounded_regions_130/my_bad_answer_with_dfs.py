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
        v = dict()
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == 'O':
                    v[(i, j)] = False

        # 中间区域没有 O
        if not v or len(v) == m * n:
            return

        # 搜索方向顺序：右-> 左 -> 下 -> 上
        xdir = [0, 0, 1, -1]
        ydir = [1, -1, 0, 0]
        all_os = []
        path = []

        def dfs(cur_x, cur_y):
            """ 深度优先搜索算法。


            深度优先搜索算法的关键点是 ：
            1、一条路走到黑。

            2、撞到南墙后回头（递归的出栈过程）

            3、然后找下一条可行路径 （满足状态、剪枝、边界条件）。

            # 编写要点：一般为递归算法；需要入参；根据当前位置参数，决定下一步搜索路径。

            得到的搜索路径取决于寻路策略（程序灵活定义）


            :param cur_x: 当前坐标 x
            :param cur_y: 当前左边 y
            :return:
            """
            new_poses = [(cur_x + xdir[i], cur_y + ydir[i]) for i in range(4)]
            for new_x, new_y in new_poses:
                if (new_x in range(m) and new_y in range(n) and
                        not v.get((new_x, new_y)) and
                        board[new_x][new_y] == 'O'):

                    v[(new_x, new_y)] = True
                    path.append((new_x, new_y))

                    dfs(new_x, new_y)

                    v[(new_x, new_y)] = False

        """
        分别从不同的起始点搜索(每个搜索起点都会遍历一条完整相互连接的 O 区域）：   
        一旦发现新的搜索起点已经在已有的遍历路径中时，放弃该起点。            
        也就是说，联通的 O 区域只会搜索一次。比如如下地图：
              0    1    2    3   
        0  [['X', 'X', 'X', 'X'],
        1   ['X', 'O', 'O', 'X'],
        2   ['X', 'X', 'O', 'O'],
        3   ['X', 'O', 'X', 'X']]
        
        从 （1，1）作为起始点深度优先遍历出一条路径：
        [(1, 1)->(1, 2)-> (2, 2)-> (2, 3)] 是一片联通的 O 区域。
        下次从 (1,2)、（2，2），（2，3） 作为起始点搜索时，会发现起始点已经在已有
        遍历路径中，直接跳过。深度优先搜索 'O'最终会得到两条路径：
        [(1, 1)->(1, 2)-> (2, 2)-> (2, 3)] & [(3,1)]
        
        如下地图：
              0    1    2    3   
         0 [['X', 'X', 'X', 'X'],
         1  ['X', 'O', 'O', 'X'],
         2  ['X', 'X', 'O', 'O'],
         3  ['X', 'O', 'X', 'X']]
         
         深度优先搜索也会得到两条遍历路径
         [[(1, 1), (1, 2), (2, 2), (2, 3)], 
         [(3, 1)]]
                          
        """
        def is_in_previous_path(point):
            for pth in all_os:
                if point in pth:
                    return True
            return False

        for x, y in v:
            # 已经在搜索过的路径中，不再搜索。
            if is_in_previous_path((x,y)):
                continue

            # 放弃边界起始点
            if x in [0, m-1] or y in [0, n-1]:
                continue

            # 起始点状态标记为访问过。
            v[(x, y)] = True
            path.append((x, y))

            dfs(x, y)

            # 恢复状态
            v[(x, y)] = False
            # 至此，所有点的状态标记为位访问过。
            all_os.append(path[:])
            path.clear()


        for os_path in all_os:
            if not list(filter(lambda pos: pos[0] in [0, m - 1]
                                           or pos[1] in [0, n - 1], os_path)):
                for x, y in os_path:
                    board[x][y] = 'X'



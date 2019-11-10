# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/20 16:28 
"""


class Solution:
    def calculateMinimumHP(self, dungeon: list) -> int:
        m, n = len(dungeon), len(dungeon[0])

        # dp[x][y] 表示勇士到达 （x,y) 坐标时最低需要的健康值
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for x in range(m):
            for y in range(n):
                if dungeon[x][y] >= 0:
                    dp[x][y] = 1  # 至少需要1个健康值进入房间
                else:
                    # 比如进入该房间会损失 3 点健康值，
                    # 那么进入该房间至少需要 4 点健康值
                    dp[x][y] = 1 - dungeon[x][y]  #

        # 从地图右下角 (倒数第 1 列 倒数第一行) 逐个扫描计算
        for y in range(n - 1, -1, -1):  # 按列

            for x in range(m - 1, -1, -1):  # 按行
                if y == n - 1 and x == m - 1:  # 跳过 最右下角
                    continue

                """
                最后一列（dungenon[m-1][n-1]除外）每一格的健康值只受到其下方健
                康值和进入房间初始健康值的约束
                dp[x][y] + dungeon[x][y] = dp[x+1][y] =>
                dp[x][y] = dp[x+1][y] - dungeon[x][y]
                """
                if y == n - 1:
                    dp[x][y] = max(dp[x][y], dp[x + 1][y] - dungeon[x][y])
                    continue

                """
                第1列至倒数第二列每一格的健康值只受到其右方健康值和进入房间初始
                健康值的约束
                dp[x][y] + dungeon[x][y] = dp[x][y+1] =>
                dp[x][y] = dp[x][y+1] - dungeon[x][y]
                """
                right_min = dp[x][y + 1] - dungeon[x][y]
                if x == m - 1:
                    dp[x][y] = max(dp[x][y], right_min)
                    continue

                """
                第1列至倒数第二列,第一行到倒数第二行中，每一格的健康值同时受到
                其右方健康值、下方健康值 和进入房间初始健康值的约束
                dp[x][y] + dungeon[x][y] = dp[x+1][y] =>
                dp[x][y] = dp[x+1][y] - dungeon[x][y]
                """
                down_min = dp[x + 1][y] - dungeon[x][y]
                neighbor_min = min(right_min, down_min)  # 此处有1条路可走即可
                dp[x][y] = max(dp[x][y], neighbor_min)

        return dp[0][0]

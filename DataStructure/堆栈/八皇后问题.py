# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 八皇后问题.py 
@time: 2018/8/12 10:17 
"""
from pprint import pprint as P


class QueenGame(object):
    def __init__(self, n=8):
        self.N = n
        self.queen_row_num = [None] * self.N  # 记录N列上皇后所在行，数组下标为列；数组值为行。
        self.solution_num = 0

    def print_table(self):
        x, y = 0, 0
        num = self.solution_num
        print('%s皇后问题的第%d组解\t' % (self.N, num))

        for x in range(self.N):  # 遍历行
            for y in range(self.N):  # 遍历列
                if x == self.queen_row_num[y]:
                    print('<Q>', end='')
                else:
                    print('<->', end='')
            print('\t')

        # input('\n..请按任意键继续...\n')

    def can_be_attacked(self, row, col):
        """判断第row行，第col列上的皇后是否能被其以左的列上的

        任意一个皇后攻击到（同一行或者对角线上）

        :param row:
        :param col:
        :return:
        """
        i = 0
        while i < col:
            col_offset = abs(i - col)
            row_offset = abs(self.queen_row_num[i] - row)

            # 同一行上 或对角线上
            if row_offset == 0 or col_offset == row_offset:  # 对角线上
                return True

            i += 1
        return False

    def put_queen(self, col):
        """放置第col列上皇后的位置（递归算法）

        :param col:
        :return:
        """
        i = 0
        while i < self.N: # 从第一行开始放置，如果不行就放到下一行，以此类推。
            if not self.can_be_attacked(i, col): #判断放置在第i行是否OK。
                self.queen_row_num[col] = i  # 记录第col列皇后的行号.

                if col == self.N - 1: # 所有列皇后都已经放置OK
                    self.solution_num += 1
                    # self.print_table()
                else: # 摆放下一列的皇后
                    self.put_queen(col + 1)

            i += 1


if __name__ == '__main__':
    game = QueenGame(12)
    game.put_queen(0)
    print(game.solution_num)

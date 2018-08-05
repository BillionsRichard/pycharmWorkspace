# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 堆栈的应用-迷宫游戏.py 
@time: 2018/8/5 18:18 
"""
from pprint import pprint as pp


class NoLimitArrayStack(object):
    """利用数组（列表）实现的无穷大的堆栈数据结构（栈顶指针指向栈顶元素）

    """
    INIT_SIZE = 10

    def __init__(self):
        self.MAX_SIZE = NoLimitArrayStack.INIT_SIZE
        self.top = -1
        self.data_list = [None] * self.MAX_SIZE

    def push(self, data):
        if self.is_full():
            print('Full Error.')
            return

        self.top += 1
        self.data_list[self.top] = data

    def pop(self):
        if self.is_empty():
            print('Emtpy Error')
            return None

        pop_data = self.data_list[self.top]
        self.top -= 1
        # print('poped:%s' % str(pop_data))
        return pop_data

    def is_full(self):
        if self.top == self.MAX_SIZE - 1:
            self.expand_capacity()

        return False

    def expand_capacity(self):
        capacity_size = 2 * self.MAX_SIZE
        self.data_list.extend([None] * capacity_size)
        self.MAX_SIZE += capacity_size
        return

    def is_empty(self):
        return self.top == -1

    def top_data(self):
        if not self.is_empty():
            return self.data_list[self.top]
        return None


class MazeGame(object):
    def __init__(self, row_num, col_num, start_position, end_position):
        self.maze = self.generate_map(col_num, row_num)
        self.start_position = start_position
        self.exit_position = end_position
        self.path_stack = NoLimitArrayStack()

        self.MAX_X = row_num - 1
        self.MAX_Y = col_num - 1

        pp(self.maze)

    def generate_map(self, col_num, row_num):
        maze = []
        for i in range(row_num):
            maze.append([])
            for j in range(col_num):
                maze[i].append(1)
                if j in range(1, 4) and i == 1:
                    maze[i][j] = 0

                if j in range(6, 11) and i == 2:
                    maze[i][j] = 0

                if j in range(3, 7) and i == 4:
                    maze[i][j] = 0

                if j in range(1, 10) and i == 9:
                    maze[i][j] = 0

                if i in range(1, 7) and j == 3:
                    maze[i][j] = 0

                if i in range(1, 10) and j == 6:
                    maze[i][j] = 0

                if i in range(2, 11) and j == 11:
                    maze[i][j] = 0
        return maze

    def is_exit_point(self, x, y):
        return (x, y) == self.exit_position

    def can_walk_to(self, x, y):
        return self.maze[x][y] == 0

    def start_walk(self):
        maze = self.maze
        x, y = self.start_position

        while x <= self.MAX_X and y <= self.MAX_Y:
            maze[x][y] = 2

            if self.can_walk_to(x - 1, y):  # 向上走一步
                x -= 1
                self.path_stack.push((x, y))

            elif self.can_walk_to(x + 1, y):  # 向下走一步
                x += 1
                self.path_stack.push((x, y))

            elif self.can_walk_to(x, y - 1):  # 向左走一步
                y -= 1
                self.path_stack.push((x, y))

            elif self.can_walk_to(x, y + 1):  # 向右走一步
                y += 1
                self.path_stack.push((x, y))

            elif self.is_exit_point(x, y):
                break

            else:
                self.path_stack.pop()
                stack_top = self.path_stack.top_data()
                if not stack_top:
                    raise Exception("Oops, no entry point???")

                x, y = stack_top


if __name__ == '__main__':
    game = MazeGame(12, 13, (1, 1), (10, 11))
    game.start_walk()
    path_stack = game.path_stack
    all_path = []

    while not path_stack.is_empty():
        all_path.append(path_stack.pop())

    pp(list(reversed(all_path)))

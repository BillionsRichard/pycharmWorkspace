# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/12/8 15:21
"""


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """


class Solution:
    def cleanRoom(self, robot: Robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def get_up_step(cur_up=0, cur_left=0, dirs=[]):
            while robot.move():
                dirs.append('u')
                cur_up += 1

            robot.turnLeft()
            if robot.move():  # 可以向左
                cur_left += 1
                dirs.append('l')

                robot.turnRight()
                return get_up_step(cur_up, cur_left, dirs)
            else:
                robot.turnRight()
                return cur_up, cur_left

        def search_up_left(dir_step_dict, cur_dir):
            # move upward util can not move
            if cur_dir == 'u':
                while robot.move():
                    dir_step_dict['u'] += 1

                robot.turnLeft()  # left
                if robot.move():  # left direction
                    dir_step_dict['l'] += 1
                    search_up_left(dir_step_dict, cur_dir='l')

            elif cur_dir == 'l':
                robot.turnRight()
                search_up_left(dir_step_dict, cur_dir='u')

            else:  # cur_dir == 'd'
                robot.turnLeft()  # down direction
                if robot.move():
                    dir_step_dict['d'] += 1
                    robot.turnRight()  # left direction
                    if robot.move():
                        dir_step_dict['l'] += 1
                        robot.turnRight()  # up direction
                        search_up_left(dir_step_dict)
                    else:
                        robot.move()

                    robot.turnRight()
                    if
                        search_up_left(dir_step_dict)
                else:
                    robot.turnRight()
                    robot.turnRight()
                    return

        from collections import defaultdict
        dir_step_dict = defaultdict(int)
        search_up_left(dir_step_dict)
        print(dir_step_dict)

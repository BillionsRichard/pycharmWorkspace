# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 堆栈的数组实现.py 
@time: 2018/8/5 14:19 
"""


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
        print('poped:%s' % pop_data)
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


if __name__ == '__main__':
    s = NoLimitArrayStack()

    print('is full:%s' % s.is_full())
    print('is empty:%s' % s.is_empty())

    s.push('sam')
    s.push('cheung')
    s.push('ada')
    s.pop()
    s.push('a')
    s.push('b')
    s.push('c')
    s.push('d')
    s.push('e')
    s.push('f')
    s.push('G')
    s.push('I')
    s.push('H')
    s.push('J')

    while not s.is_empty():
        s.pop()

    for i in range(pow(2, 20)):
        s.push(i)

    while not s.is_empty():
        s.pop()

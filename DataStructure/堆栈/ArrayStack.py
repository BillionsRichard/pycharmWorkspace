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


class ArrayStack(object):
    """利用数组（列表）实现的堆栈数据结构（栈顶指针指向栈顶元素）

    """

    def __init__(self, stack_size=100):
        self.MAX_SIZE = stack_size
        self.top = -1
        self.data_list = [None] * self.MAX_SIZE

    def push(self, data):
        if self.is_full():
            print('Full Error:%s' % data)
            return

        self.top += 1
        self.data_list[self.top] = data

    def pop(self):
        if self.is_empty():
            print('Emtpy Error')
            return None

        pop_data = self.data_list[self.top]
        self.data_list[self.top] = None
        self.top -= 1
        print('poped:%s' % pop_data)
        return pop_data

    def is_full(self):
        return self.top == self.MAX_SIZE - 1

    def is_empty(self):
        return self.top == -1

    def top_data(self):
        if self.is_empty():
            return None
        else:
            return self.data_list[self.top]


if __name__ == '__main__':
    s = ArrayStack(10)

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

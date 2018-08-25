# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:
@software: PyCharm
@file: 表达式转换.py
@time: 2018/8/18 17:29
"""
from ArrayStack import ArrayStack


class InorderMathExpression(object):
    #操作符及其优先级的映射
    OPERATOR_PRIORITY_MAP = {
        '(': 0,
        '+': 1,
        '-': 1,

        '*': 2,
        '/': 2,
        '%': 2,
        ')': 3,

    }

    def __init__(self, expression):
        self.expression = expression

    def to_post_fix(self):
        operator_stack = ArrayStack()
        post_fix_str = ''

        for token in self.expression:
            if self.is_operand(token):
                post_fix_str += token
                continue

            if ')' == token:
                while not operator_stack.is_empty():
                    poped = operator_stack.pop()
                    if poped == '(':
                        break
                    else:
                        post_fix_str += poped
                continue
            elif '(' == token:  # 左括号直接进栈
                operator_stack.push(token)
                continue

            while not operator_stack.is_empty():
                top_data = operator_stack.top_data()
                cur_priority = self.get_priority(token)
                top_priority = self.get_priority(top_data)

                if cur_priority > top_priority:
                    operator_stack.push(token)
                    break
                else:
                    post_fix_str += operator_stack.pop()
                    continue
            else:
                operator_stack.push(token)

        while not operator_stack.is_empty():
            post_fix_str += operator_stack.pop()

        return post_fix_str

    @staticmethod
    def is_operand(token):
        """判断读入的字符是否是操作数

        :param token:
        :return:
        """
        return token not in InorderMathExpression.OPERATOR_PRIORITY_MAP

    @staticmethod
    def get_priority(token):
        return InorderMathExpression.OPERATOR_PRIORITY_MAP.get(token)


if __name__ == '__main__':
    in_fix_exp = '(A+B)*D+E/(F+A*D)+C'
    inorder_exp_obj = InorderMathExpression(in_fix_exp)
    print(inorder_exp_obj.to_post_fix())
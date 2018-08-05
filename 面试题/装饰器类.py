# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:
@software: PyCharm
@file: 装饰器类.py
@time: 2018/8/1 19:22
"""
from pprint import pprint as P


class Decorator(object):
    def __init__(self, name=None):
        self.name = name
        self.func = None

    def __call__(self, func, *args, **kwargs):
        self.func = func
        print('name=%s' % self.name)
        # return self.func(*args, **kwargs)
        return self.func


@Decorator(name='CLI')
def cli(cmd, mode):
    print('cmd=%s, mode=%s' % (cmd, mode))


if __name__ == '__main__':
    cli('show system general', 'devloper')

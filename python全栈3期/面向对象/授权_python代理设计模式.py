# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 授权_python代理设计模式.py
@time: 2018/5/13 17:38 
"""
import time

class MyFile:
    def __init__(self, file_name, mode='r', encoding='utf-8'):
        self.file = open(file_name, encoding=encoding, mode=mode) # 组合（非继承）
        self.mode = mode
        self.encoding=encoding


    def __getattr__(self, item): # 找不到属性时才会调用该方法。
        print('getattr called...')
        return getattr(self.file, item)


    def write(self, line): # 类似于代理设计模式。。。
        t = time.strftime('%Y-%m-%d %X') # 注意时间的格式化

        self.file.write('%s %s' %(t, line))


f = MyFile('a.txt', 'a+')
# f.read()

f.write('hello world...,我是菜鸟一个》。。\n')
f.write('CPU 内存不足。。\n')
f.write('磁盘空间不足。。\n')

f.close()

f1 = MyFile('a.txt')
print(f1.read())

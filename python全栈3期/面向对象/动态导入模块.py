# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 动态导入模块.py 
@time: 2018/5/13 15:29 
"""

# from m1 import t

# module_t = __import__('m1.t') # 导入的是顶级模块：m1
#
# print(module_t)
#
# print(dir(module_t))
#
# module_t.t.test() # 注意调用方式。
# module_t.t.test1()
#
# from m1.t import test1, test, __test2 #私有的不能通过import * 导入.
#
# test()
# test1()
# __test2()

import importlib

t = importlib.import_module('m1.t') # 导入的就是子模块，推荐使用。

t.test()
t.test1()
t.__test2()
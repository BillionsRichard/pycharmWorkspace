# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 模块的反射.py 
@time: 2018/5/13 18:44 
"""

import test as module_obj

if hasattr(module_obj, 'say_hi'): # 反射实现功能的可插拔
    say_hi_fun = getattr(module_obj, 'say_hi')
    say_hi_fun()
else:
    print('hello world.')




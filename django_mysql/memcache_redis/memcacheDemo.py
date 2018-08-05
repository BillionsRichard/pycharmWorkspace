# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: memcacheDemo.py
@time: 2018/7/22 15:20 
"""
from pprint import pprint as P

import memcache

mc = memcache.Client(['192.168.2.123:11211'], debug=True)
mc.set("foo", "bar")
ret = mc.get('foo')
print(ret)

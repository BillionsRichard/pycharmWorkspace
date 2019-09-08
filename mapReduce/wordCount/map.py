# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: map.py 
@time: 2018/9/8 16:58 
"""
from pprint import pprint as P
import sys
import re

p = re.compile(r'\w+')
for line in sys.stdin:
    word_list = line.strip().split()
    for word in word_list:
        find_list = p.findall(word)
        if find_list:
            word = find_list[0]
            print("%s\t%s" % (word, 1))

# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: map.py 
@time: 2019/2/4 11:16 
"""
from pprint import pprint as pp
import sys
import re

for line in sys.stdin:
    for raw_word in line.split():
        words = re.findall(r'\w+', raw_word)
        if words:
            word = words[0].lower()
        else:
            continue

        if not word:
            continue
        else:
            print("%s\t%d" % (word, 1))

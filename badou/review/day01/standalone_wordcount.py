# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: standalone_wordcount.py 
@time: 2019/2/4 14:14 
"""
from pprint import pprint as pp
import re
import operator

word_cnt_map = {}
with open('data/The_Man_of_Property.txt', 'r') as f:
    for line in f:
        for word_raw in line.split():
            words = re.findall(r'\w+', word_raw)
            if words:
                word = words[0].lower()
                new_cnt = word_cnt_map.setdefault(word, 0) + 1
                word_cnt_map[word] = new_cnt

# pp(word_cnt_map)
pp(len(word_cnt_map))
pp(sorted(word_cnt_map.items(), key=operator.itemgetter(1), reverse=True)[:20])
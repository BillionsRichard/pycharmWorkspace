# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: red.py 
@time: 2018/9/8 17:11 
"""
from pprint import pprint as P
import sys

cur_word = None
word_cnt_sum = 0

for line in sys.stdin:
    word, cnt = line.split()
    if not cur_word:
        cur_word = word

    if word != cur_word:
        print('%s\t%s' % (cur_word, word_cnt_sum))
        cur_word = word
        word_cnt_sum = 0

    word_cnt_sum += int(cnt)

print('%s\t%s' % (cur_word, word_cnt_sum))